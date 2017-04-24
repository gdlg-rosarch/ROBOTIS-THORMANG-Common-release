Name:           ros-kinetic-thormang3-common
Version:        0.1.2
Release:        0%{?dist}
Summary:        ROS thormang3_common package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/thormang3_common
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-thormang3-action-module-msgs
Requires:       ros-kinetic-thormang3-feet-ft-module-msgs
Requires:       ros-kinetic-thormang3-gripper-module-msgs
Requires:       ros-kinetic-thormang3-manipulation-module-msgs
Requires:       ros-kinetic-thormang3-offset-tuner-msgs
Requires:       ros-kinetic-thormang3-walking-module-msgs
Requires:       ros-kinetic-thormang3-wholebody-module-msgs
BuildRequires:  ros-kinetic-catkin

%description
ROS packages for the thormang3_common (meta package)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Apr 24 2017 Pyo <pyo@robotis.com> - 0.1.2-0
- Autogenerated by Bloom

* Wed Aug 31 2016 pyo <pyo@robotis.com> - 0.1.1-0
- Autogenerated by Bloom

* Wed Aug 17 2016 pyo <pyo@robotis.com> - 0.1.0-0
- Autogenerated by Bloom

