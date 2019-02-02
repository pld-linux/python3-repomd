#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"

%define 	module		repomd
%define 	egg_name	repomd
%define		pypi_name	repomd
Summary:	Library for reading dnf/yum repositories
Name:		python3-%{pypi_name}
Version:	0.1.0
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	f781a03ba41afb662843aca196a221ea
URL:		https://github.com/carlwgeorge/repomd
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools >= 38.6.0
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
%{py3_sitescriptdir}/%{pypi_name}.py
%{py3_sitescriptdir}/__pycache__/*
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
