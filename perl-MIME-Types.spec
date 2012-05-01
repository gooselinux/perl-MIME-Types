Name:           perl-MIME-Types
Version:        1.28
Release:        2%{?dist}
Summary:        MIME types module for Perl

License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/MIME-Types/
Source0:        http://www.cpan.org/authors/id/M/MA/MARKOV/MIME-Types-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
MIME types are used in MIME compliant lines, for instance as part of
e-mail and HTTP traffic, to indicate the type of content which is
transmitted. Sometimes real knowledge about a mime-type is need.
This module maintains a set of MIME::Type objects, which each describe
one known mime type. There are many types defined by RFCs and vendors,
so the list is long but not complete. Please don't hestitate to ask to
add additional information.


%prep
%setup -q -n MIME-Types-%{version}
f=ChangeLog ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{perl_vendorlib}/MIME/
%{_mandir}/man3/MIME::Type*.3*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.28-2
- rebuild against perl 5.10.1

* Wed Oct  7 2009 Stepan Kasal <skasal@redhat.com> - 1.28-1
- new upstream version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.27-1
- update to 1.27

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.24-1
- update to 1.24

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.23-3
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.23-2
- rebuild for new perl

* Wed Dec 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.23-1
- bump to 1.23

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.20-2
- license tag fix

* Wed Jun 13 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.20-1
- 1.20.
- Convert docs to UTF-8.

* Tue Apr 17 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.19-2
- BuildRequire perl(Test::More).

* Mon Mar 26 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.19-1
- 1.19.
- BuildRequire perl(ExtUtils::MakeMaker).

* Wed Nov 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.18-1
- 1.18.

* Fri Sep 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.17-2
- Rebuild.

* Tue Aug 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.17-1
- 1.17.

* Sun Oct  2 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.16-1
- 1.16.

* Fri Apr  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.15-2
- 1.15.

* Tue May 25 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.13-0.fdr.3
- Require perl(:MODULE_COMPAT_*) (bug 1649).

* Mon May 17 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.13-0.fdr.2
- Sync with IANA 20040517.
- Require perl >= 1:5.6.1 for vendor install dir support.
- Use pure_install to avoid perllocal.pod workarounds.

* Sat Apr 24 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.13-0.fdr.1
- Update to 1.13 + IANA 20040424.

* Sun Feb  1 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.12-0.fdr.2
- Reduce directory ownership bloat.

* Wed Jan 21 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.12-0.fdr.1
- Update to 1.12.

* Wed Jan 14 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.11-0.fdr.1
- Update to 1.11.

* Wed Dec 31 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.10-0.fdr.2
- BuildRequires perl(Test::More).

* Fri Dec 19 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.10-0.fdr.1
- Update to 1.10.

* Thu Nov  6 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.09-0.fdr.1
- Update to 1.09.

* Tue Nov  4 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.08-0.fdr.1
- Update to 1.08.

* Sat Oct 11 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.07-0.fdr.2
- Install into vendor dirs.
- Don't use fedora-rpm-helper.
- Specfile cleanup.

* Wed Jul 30 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.07-0.fdr.1
- Update to 1.07.
- Use fedora-rpm-helper.

* Tue Jun 24 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.06-0.fdr.1
- First build.
