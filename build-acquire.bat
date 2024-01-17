Rem assumes we are running this in the Visual Studio command line environment
set current-dir=%cd%
set acquire-build-dir=C:\projects\czi\acquire-video-runtime\build

cd %acquire-build-dir%
msbuild INSTALL.vcxproj /t:Rebuild /p:Configuration=Debug /p:Platform=x64"

cd %current-dir%