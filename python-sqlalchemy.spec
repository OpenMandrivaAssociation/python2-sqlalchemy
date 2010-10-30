%define module_name SQLAlchemy

Summary:	SQL toolkit and object relational mapper for Python
Name:		python-sqlalchemy
Version:	0.6.4
Release:	%mkrel 2
License:	MIT
Group:		Development/Python
URL:		http://www.sqlalchemy.org/
Source0:	http://pypi.python.org/packages/source/S/%{module_name}/%{module_name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python-nose
%py_requires -d

%description
%{module_name} is a SQL toolkit and object relational mapper for Python. It
encourages "relational mapping" as opposed to "table mapping" and includes
enterprise-level features such as eager loading, unit-of-work object commits,
topological dependency sorting, and full usage of bind parameters. It
supports MySQL, Postgres, Oracle, and SQLite.

%prep

%setup -q -n %{module_name}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %__python setup.py install --skip-build --root=%{buildroot} --install-purelib=%{python_sitelib}

%clean
%__rm -rf %{buildroot}

#%check
#%__python setup.py test

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE README doc/* examples
%{python_sitelib}/sqlalchemy/
%{python_sitelib}/%{module_name}-%{version}-py*.egg-info/
