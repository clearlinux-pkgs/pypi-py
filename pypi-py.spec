#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-py
Version  : 1.11.0
Release  : 91
URL      : https://files.pythonhosted.org/packages/98/ff/fec109ceb715d2a6b4c4a85a61af3b40c723a961e8828319fbcb15b868dc/py-1.11.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/98/ff/fec109ceb715d2a6b4c4a85a61af3b40c723a961e8828319fbcb15b868dc/py-1.11.0.tar.gz
Summary  : library with cross-python path, ini-parsing, io, code, log facilities
Group    : Development/Tools
License  : MIT
Requires: pypi-py-license = %{version}-%{release}
Requires: pypi-py-python = %{version}-%{release}
Requires: pypi-py-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pytest
Provides: py
Provides: py-python
Provides: py-python3

%description
.. image:: https://img.shields.io/pypi/v/py.svg
:target: https://pypi.org/project/py

%package license
Summary: license components for the pypi-py package.
Group: Default

%description license
license components for the pypi-py package.


%package python
Summary: python components for the pypi-py package.
Group: Default
Requires: pypi-py-python3 = %{version}-%{release}

%description python
python components for the pypi-py package.


%package python3
Summary: python3 components for the pypi-py package.
Group: Default
Requires: python3-core
Provides: pypi(py)

%description python3
python3 components for the pypi-py package.


%prep
%setup -q -n py-1.11.0
cd %{_builddir}/py-1.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642463410
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest --verbose || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-py
cp %{_builddir}/py-1.11.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-py/cf3eaf29116a37a7d9ba773e776104c067c8e5fc
cp %{_builddir}/py-1.11.0/py/_vendored_packages/apipkg-2.0.0.dist-info/LICENSE %{buildroot}/usr/share/package-licenses/pypi-py/82dbfd684f7c04da81d4faa852c6317142daa3e7
cp %{_builddir}/py-1.11.0/py/_vendored_packages/iniconfig-1.1.1.dist-info/LICENSE %{buildroot}/usr/share/package-licenses/pypi-py/cf3eaf29116a37a7d9ba773e776104c067c8e5fc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-py/82dbfd684f7c04da81d4faa852c6317142daa3e7
/usr/share/package-licenses/pypi-py/cf3eaf29116a37a7d9ba773e776104c067c8e5fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
