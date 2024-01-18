# Micro-manager - acquire test script
import time

from numpy import ndarray
from pymmcore_plus import CMMCorePlus

# global parameters
# we are not providing full paths because we are using pymmcore_plus default path
demo_mm_configuration = "MMConfig_demo.cfg"
demo_acquire_single_configuration = "acquire-demo-single.cfg"
demo_acquire_dual_configuration = "acquire-demo-dual.cfg"
live_stream = False

# file paths
data_root = "C:\\acqData\\czi\\mdi-test1"
data_prefix = "expA"


# print image info
def image_info(image: ndarray) -> str:
    return f"{img.shape}, {img.dtype}"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    system_config = demo_acquire_single_configuration

    print("Starting test...")
    core = CMMCorePlus()
    print("API: " + core.getAPIVersionInfo())
    print("VER: " + core.getVersionInfo())

    core.enableDebugLog(True)

    # load configuration
    print(f"loading configuration {system_config}...")
    core.loadSystemConfiguration(system_config)

    # exposure
    print(f"Default exposure: {core.getExposure()} ms")

    acq_exposure = 40.0
    core.setExposure(acq_exposure)
    print(f"Exposure set to {core.getExposure()} ms")

    # set up file saving
    """
    0 - AcqOrderMode.TIME_POS_SLICE_CHANNEL
    1 - AcqOrderMode.TIME_POS_CHANNEL_SLICE
    2 - AcqOrderMode.POS_TIME_SLICE_CHANNEL
    3 - AcqOrderMode.POS_TIME_CHANNEL_SLICE
    """

    num_frames = 5
    acquire = core.getCameraDevice()
    core.setProperty(acquire, "ZarrChannels", 1)
    core.setProperty(acquire, "ZarrSlices", 1)
    core.setProperty(acquire, "ZarrFrames", num_frames)
    core.setProperty(acquire, "ZarrPositions", 1)
    core.setProperty(acquire, "ZarrOrder", 0)

    core.setProperty(acquire, "StreamFormat", "Zarr")
    core.setProperty(acquire, "SaveRoot", data_root)
    core.setProperty(acquire, "SavePrefix", data_prefix)

    # acquire images
    interval_s = 1.0

    print("acquiring...")
    input("Press Enter to continue...")

    core.setProperty(acquire, "SaveToZarr", "1")

    if live_stream:
        print("Running live sequence...")
        core.startSequenceAcquisition(num_frames, 0, False)
    else:
        for i in range(num_frames):
            core.snapImage()
            img = core.getImage()
            print(f"\timage {i + 1}: {image_info(img)}")
            time.sleep(interval_s)

    core.setProperty(acquire, "SaveToZarr", "0")
    print(f"Done. Data saved in {data_root}\\{data_prefix}")
