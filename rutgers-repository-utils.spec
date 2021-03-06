%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:		rutgers-repository-utils
Version:	1.3
Release:	1%{?dist}
Summary:	Python scripts for miscellaneous repository management
Group:		System Environment/Base
License:	GPLv2+
URL:		https://github.com/oss/rutgers-repository-utils
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch

Provides:       createrepo
Provides:       repoclosure
Requires:	yum-utils
Requires:       centos-release
Requires:       python
BuildRequires:	python

%description
These Python scripts are based on yum-utils and createrepo. Together, they
create repository directories and do dependency checking.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --skip-build --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{python_sitelib}/rutgers-repository-utils/
%{python_sitelib}/rutgers_repository_utils-%{version}-py2.6.egg-info

%changelog
