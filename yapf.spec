
Summary: A formatter for Python code.
Name: yapf
Version: 0.1
Release: 1
Source0: %{name}-%{version}.tar.gz
License: Apache License, Version 2.0
Group: Development/Libraries
BuildArch: noarch
Vendor: Bill Wendling <morbo@google.com>

%description
====
YAPF
====


%prep
%setup -n %{name}-%{version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Fri Apr 03 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.1
- Initial Spec File creation
