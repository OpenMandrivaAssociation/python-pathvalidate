Name:      python-pathvalidate
Version:   3.3.1
Release:   3
Summary:   Library to sanitize/validate a string such as file-names/file-paths/etc
License:   MIT
Group:     Development/Python
URL:       https://github.com/thombashi/pathvalidate
Source:    https://files.pythonhosted.org/packages/source/p/pathvalidate/pathvalidate-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
#BuildRequires:  python-pytest
#BuildRequires:  python-allpairspy
BuildRequires:  python%{pyver}dist(click)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
# Needed for version metadata (pyproject [tool.setuptools_scm]); without it
# the wheel is pathvalidate-0.0.0 and Provides becomes python3.Xdist(pathvalidate) = 0
BuildRequires:  python%{pyver}dist(setuptools-scm)
#BuildRequires:  python-tcolorpy

%description
%{summary}.
%prep
%autosetup -n pathvalidate-%{version} -p1

%build
# The sdist is not a git checkout. Without this the wheel version is 0.0.0.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py_build

%install
%py_install

%files
%doc README.rst
%{python_sitelib}/pathvalidate-%{version}.dist-info
%{python_sitelib}/pathvalidate/
