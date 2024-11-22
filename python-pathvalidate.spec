Name:      python-pathvalidate
Version:   3.2.1
Release:   1
Summary:   Library to sanitize/validate a string such as file-names/file-paths/etc
License:   MIT
URL:       https://github.com/thombashi/pathvalidate
Source:    https://files.pythonhosted.org/packages/source/p/pytube/pathvalidate-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
#BuildRequires:  python-pytest
#BuildRequires:  python-allpairspy
BuildRequires:  python-click
#BuildRequires:  python-tcolorpy

%description
%{summary}.
%prep
%autosetup -n pathvalidate-%{version} -p1

%build
%py_build

%install
%py_build

%files
%doc README.rst
