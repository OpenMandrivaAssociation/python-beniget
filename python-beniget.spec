%define module beniget

Name:		python-beniget
Version:	0.5.0
Release:	2
Summary:	Extract semantic information about static Python code
Group:		Development/Python
License:	BSD
URL:		https://github.com/serge-sans-paille/beniget/
Source0:	https://github.com/serge-sans-paille/beniget/archive/%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(gast)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Beniget is a static analyzer for Python2 and Python3 code.

Beniget provides a static over-approximation of the global and local
definitions inside Python Module/Class/Function. It can also compute
def-use chains from each definition.

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}-*.*-info
