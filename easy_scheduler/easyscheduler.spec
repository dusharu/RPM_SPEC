########## VAR
%define rel_ver 1.9.8
%define rpm_ver 1
# disable repack .jar
%define __jar_repack %{nil}

########## Descr
Summary: visual control tool for running console applications on remote servers.
Name: easyscheduler
Version: %{rel_ver}
Release: %{rpm_ver}
ExclusiveArch: x86_64
License: Community
Group: Applications/Databases
URL: http://easydata.ru/product/easyscheduler/
Source0: http://easydata.ru/download/easyportal/scheduler-%{rel_ver}.zip
BuildRoot: %{_tmppath}/%{name}-%{rel_ver}-%{release}-root
BuildRequires: unzip
#Requires: java-1.8.0-openjdk
AutoReqProv: no

%description
EasyScheduler is a visual control tool for running console applications on remote servers.
It enables to schedule the launch at pre-defined time or after specified time intervals,
monitor task progress, keep logs and automatically load files
to run console applications on remote servers.

%package EasyScheduler
Summary: EasyScheduler - server
Group: Applications/Databases

%description EasyScheduler
EasyScheduler is a visual control tool for running console applications on remote servers.
It enables to schedule the launch at pre-defined time or after specified time intervals,
monitor task progress, keep logs and automatically load files
to run console applications on remote servers.

%package EasyRuntime
Summary: EasyRuntime - client for EasyScheduler
Group: Applications/Databases

%description EasyRuntime
EasyScheduler is a visual control tool for running console applications on remote servers.
It enables to schedule the launch at pre-defined time or after specified time intervals,
monitor task progress, keep logs and automatically load files
to run console applications on remote servers.

%prep

%build

%install
# install EasyScheduler 
mkdir -p %{buildroot}/opt/easyportal
unzip %{SOURCE0} -d %{buildroot}/opt/easyportal
mkdir -p %{buildroot}/etc/init.d
cp %{buildroot}/opt/easyportal/scheduler/daemon/easy-scheduler %{buildroot}/etc/init.d/easy-scheduler

# install EasyRuntime
mkdir -p  %{buildroot}/opt/easyportal/runtime
unzip %{buildroot}/opt/easyportal/scheduler/storage/runtime/launcher.zip -d %{buildroot}/opt/easyportal
cp %{buildroot}/opt/easyportal/runtime/daemon/easy-runtime %{buildroot}/etc/init.d/easy-runtime
# remove lib for non x86_64 arch
for FILE in %{buildroot}/opt/easyportal/runtime/lib/sigar/*; do
  if ! echo "$FILE" | grep amd64-linux &>/dev/null ; then
    rm -f "$FILE"
  fi
done

%clean
rm -rf %{buildroot}

%files EasyScheduler
%defattr(-,easyportal,easyportal,-)
%dir %attr(0750, easyportal, easyportal)  /opt/easyportal
%dir %attr(0750, easyportal, easyportal)  /opt/easyportal/scheduler
/opt/easyportal/scheduler/*
%attr(0755, root, root) /etc/init.d/easy-scheduler

%files EasyRuntime
%defattr(-,easyportal,easyportal,-)
%dir %attr(0750, easyportal, easyportal)  /opt/easyportal
%dir %attr(0750, easyportal, easyportal)  /opt/easyportal/runtime
/opt/easyportal/runtime/
%attr(0755, root, root) /etc/init.d/easy-runtime



%pre
getent group easyportal >/dev/null || groupadd -r easyportal
getent passwd easyportal >/dev/null || useradd -r -g easyportal -d /opt/easyportal -s /sbin/nologin easyportal

%post

%preun
service easy-scheduler stop

%postun

%changelog
* Fri Feb 7 2020 Andrey Laykov  <dusharu17@gmail.om> - 1.9.8
- create rpm