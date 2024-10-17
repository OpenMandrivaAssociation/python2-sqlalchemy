%define debug_package %{nil}
%define module_name SQLAlchemy

Summary:	SQL toolkit and object relational mapper for Python

Name:		python2-sqlalchemy
Version:	0.9.8
Release:	2
License:	MIT
Group:		Development/Python
Url:		https://www.sqlalchemy.org/
Source0:	http://pypi.python.org/packages/source/S/SQLAlchemy/SQLAlchemy-%{version}.tar.gz
BuildRequires:	python2-nose
BuildRequires:	python2-setuptools
BuildRequires:	pkgconfig(python2)

%description
%{module_name} is a SQL toolkit and object relational mapper for Python. It
encourages "relational mapping" as opposed to "table mapping" and includes
enterprise-level features such as eager loading, unit-of-work object commits,
topological dependency sorting, and full usage of bind parameters. It
supports MySQL, Postgres, Oracle, and SQLite.

%prep

%setup -qn %{module_name}-%{version}

%build
%__python2 setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python2 setup.py install --skip-build --root=%{buildroot} --install-purelib=%{py2_platlibdir}

#%check
#%__python setup.py test

%files
%doc CHANGES LICENSE README* doc/* examples
%{py2_platsitedir}/sqlalchemy/*
%{py2_platsitedir}/%{module_name}-%{version}-py*.egg-info/
#{python_sitelib}/sqlalchemy_nose/
