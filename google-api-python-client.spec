Name:           google-api-python-client
Version:        1.2
Release:        1%{?dist}
Summary:        Google API Client Library for Python

Group:          Development/Languages
License:        Apache 2.0
URL:            http://code.google.com/p/google-api-python-client/
Source0:        https://google-api-python-client.googlecode.com/files/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-setuptools


%description
The Google API Client for Python is a client library for
accessing the Plus, Moderator, and many other Google APIs.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG FAQ LICENSE README
%{python_sitelib}/*

%changelog
* Sun Sep 21 2014 Eugene Zamriy <eugene@zamriy.info> - 1.2-1
- Initial release: 1.2 version
