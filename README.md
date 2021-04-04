GeNeric_build is a set of toolchains for gn. It is designed to become the "build" directory of a project.

Right now, only Windows is supported, and there are no additional options for build & linker flags. Additionally, to actually build on Windows using ninja, you will need to use the relevant vsvars.bat script in a Visual Studio installation in order for the linker to pull in the necessary libs.

Note that, since the toolchain and buildconfig files contain large parts copied from the Chromium code base, it falls under the same license (in this case, BSD). I do not plan to add any additional licensing on it, and this GeNeric_build repo can be considered licensed under BSD.
