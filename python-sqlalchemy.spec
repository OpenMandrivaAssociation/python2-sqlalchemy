%define module_name SQLAlchemy
%ifarch %arm %mips
%define debug_package %nil
%endif

Summary:	SQL toolkit and object relational mapper for Python
Name:		python-sqlalchemy
Version:	0.8.2
Release:	1
License:	MIT
Group:		Development/Python
URL:		http://www.sqlalchemy.org/
Source0:	http://pypi.python.org/packages/source/S/SQLAlchemy/SQLAlchemy-%{version}.tar.gz
BuildRequires:	python-setuptools
BuildRequires:	python-nose
BuildRequires:	python-devel

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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --skip-build --root=%{buildroot} --install-purelib=%{py_platlibdir}

#%check
#%__python setup.py test

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE README* doc/* examples
%{py_platsitedir}/sqlalchemy/*
%{py_platsitedir}/%{module_name}-%{version}-py*.egg-info/
#%{python_sitelib}/sqlalchemy_nose/
