%define module_name SQLAlchemy

Summary:	SQL toolkit and object relational mapper for Python
Name:		python-sqlalchemy
Version:	0.7.9
Release:	2
License:	MIT
Group:		Development/Python
URL:		http://www.sqlalchemy.org/
Source0:	http://pypi.python.org/packages/source/S/SQLAlchemy/SQLAlchemy-%{version}.tar.gz
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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --skip-build --root=%{buildroot} --install-purelib=%{python_sitelib}

#%check
#%__python setup.py test

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE README* doc/* examples
%{python_platlib}/sqlalchemy/*
%{python_platlib}/%{module_name}-%{version}-py*.egg-info/
#%{python_sitelib}/sqlalchemy_nose/


%changelog
* Mon May 02 2011 Michael Scherer <misc@mandriva.org> 0.6.6-1mdv2011.0
+ Revision: 661938
- fix build on x86_64

  + Sandro Cazzaniga <kharec@mandriva.org>
    - re-fix file list
    - fix file list
    - update to 0.6.6
    - update file list

* Mon Nov 01 2010 Funda Wang <fwang@mandriva.org> 0.6.4-3mdv2011.0
+ Revision: 591429
- rebuild for py 2.7

* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 0.6.4-2mdv2011.0
+ Revision: 590593
- rebuild for python 2.7

* Tue Sep 07 2010 Lev Givon <lev@mandriva.org> 0.6.4-1mdv2011.0
+ Revision: 576682
- Update to 0.6.4.
- Update to 0.6.2.
- Update to 0.6.1.

* Mon Jan 18 2010 Frederik Himpe <fhimpe@mandriva.org> 0.5.8-1mdv2010.1
+ Revision: 493276
- update to new version 0.5.8

* Tue Dec 29 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.7-1mdv2010.1
+ Revision: 483307
- update to new version 0.5.7

* Mon Sep 14 2009 Lev Givon <lev@mandriva.org> 0.5.6-1mdv2010.0
+ Revision: 441080
- Update to 0.5.6.

* Tue Jul 14 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.5-1mdv2010.0
+ Revision: 396016
- update to new version 0.5.5

* Wed May 27 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.4p2-1mdv2010.0
+ Revision: 380279
- update to new version 0.5.4p2

* Mon May 18 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.4p1-1mdv2010.0
+ Revision: 377349
- update to new version 0.5.4p1

* Sat May 02 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.3-1mdv2010.0
+ Revision: 370658
- update to new version 0.5.3

* Sun Mar 15 2009 Michael Scherer <misc@mandriva.org> 0.5.2-1mdv2009.1
+ Revision: 355347
- update to new version
- do not hardcode the module name everywhere
- use a different source url to ease update with mdvsys

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 0.4.8-2mdv2009.1
+ Revision: 323373
- rebuild

* Thu Nov 13 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.8-1mdv2009.1
+ Revision: 302684
- 0.4.8

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 0.4.7p1-1mdv2009.0
+ Revision: 280565
- New version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.4.6-2mdv2009.0
+ Revision: 269043
- rebuild early 2009.0 package (before pixel changes)

* Wed Jun 11 2008 Lev Givon <lev@mandriva.org> 0.4.6-1mdv2009.0
+ Revision: 218094
- Update to 0.4.6.

* Thu Feb 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.11-1mdv2008.1
+ Revision: 173632
- fix build deps (duh!)
- import python-sqlalchemy


* Thu Feb 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.11-1mdv2008.1
- initial Mandriva package

* Sun Jan 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.11-1.RHEL4
- initial Redhat RHEL4 package.

