#
# Conditional build:
%bcond_without	tests	# unit tests

%define 	module		repomd
%define 	egg_name	repomd
%define		pypi_name	repomd
Summary:	Library for reading dnf/yum repositories
Summary(pl.UTF-8):	Biblioteka do odczytu repozytoriów dnf/yum
Name:		python3-%{pypi_name}
Version:	0.2.1
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/r/repomd/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	3979bcf59644ead9fb3324fe36d183ed
URL:		https://github.com/carlwgeorge/repomd
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools >= 1:38.6.0
%if %{with tests}
BuildRequires:	python3-lxml
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides an object-oriented interface to get information
out of dnf/yum repositories.

%description -l pl.UTF-8
Ta biblioteka udostępnia obiektowo zorientowany interfejs do
pobierania informacji z repozytoriów dnf/yum.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__/%{module}.cpython-*.py[co]
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
