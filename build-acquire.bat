Rem assuming we are running this in the Visual Studio command line environment

Rem build acquire
set current-dir=%cd%
set acquire-build-dir=C:\projects\czi\acquire-video-runtime\build
set acquire-install-dir=C:\projects\czi\acquire-video-runtime\install
set mm-3rdparty-dir=C:\projects\3rdparty\CZI\acquire
set mm-adapter-dir=C:\projects\micro-manager\mmCoreAndDevices\DeviceAdapters\Acquire
set mm-runtime-dir=C:\Program Files\Micro-manager-2.0
set config=Debug
set acq-target=Build
set mm-target=Rebuild
set platform=x64

cd %acquire-build-dir%
msbuild INSTALL.vcxproj /t:%acq-target% /p:Configuration=%config% /p:Platform=%platform%"

Rem copy acquire libraries and includes to micro-manager 3rdparty
if %config% == Release copy %acquire-install-dir%\lib\*.* %mm-3rdparty-dir%\lib
if %config% == Debug copy %acquire-install-dir%\lib\*.* %mm-3rdparty-dir%\Debug\lib
xcopy %acquire-install-dir%\include\*.* %mm-3rdparty-dir%\include /s /Y

Rem build micro-manager Acquire adapter
msbuild %mm-adapter-dir%\Acquire.vcxproj /t:%mm-target% /p:Configuration=%config% /p:Platform=%platform%

Rem copy adapter to micro-manager run time dir
copy %mm-adapter-dir%\build\%config%\%platform%\mmgr_dal_Acquire.dll "%mm-runtime-dir%"
echo Build completed

cd %current-dir%