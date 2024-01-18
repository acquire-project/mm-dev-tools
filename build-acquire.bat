Rem assuming we are running this in the Visual Studio command line environment

set current-dir=%cd%
set acquire-build-dir=C:\projects\czi\acquire-video-runtime\build
set acquire-install-dir=C:\projects\czi\acquire-video-runtime\install
set mm-3rdparty-dir=C:\projects\3rdparty\CZI\acquire
set config=Debug
set target=Build

cd %acquire-build-dir%
msbuild INSTALL.vcxproj /t:%target% /p:Configuration=%config% /p:Platform=x64"

if %config% == Release copy %acquire-install-dir%\lib\*.* %mm-3rdparty-dir%\lib
if %config% == Debug copy %acquire-install-dir%\lib\*.* %mm-3rdparty-dir%\Debug/lib
xcopy %acquire-install-dir%\include\*.* %mm-3rdparty-dir%\include /s /Y

cd %current-dir%