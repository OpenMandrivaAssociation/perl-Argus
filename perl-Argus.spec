%define argus_version 2.0.6.fixes.1

Name:		perl-Argus
Version:	%perl_convert_version 3.0.7.14
Release:	1
Epoch:		0
Summary:	Client tools for argus network audit
License:	GPL
Group:		Development/Perl
Url:		http://qosient.com/argus/
Source0:	ftp://ftp.qosient.com:21/dev/argus-3.0/argus-clients-%{version}.tar.gz

BuildRequires:	 perl-devel
BuildRequires:	 perl-DateManip
Provides:	perl(Argus::Support)
BuildArch:	noarch

%description
Clients to the argus probe which process and display information.

%prep
%setup -q -n argus-clients-%{argus_version}/contrib/Argus-perl-%{version}
export ARGUSHOME=%{_prefix}
perl Makefile.PL PREFIX=%{_prefix} INSTALLSITELIB=%{perl_vendorlib}
perl -pi -e 's|local/||g' Makefile

%build
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_prefix}/perllocal.pod

%files
%defattr(0644,root,root,0755)
%doc HISTORY INSTALL README TODO
%attr(0755,root,root) %{_bindir}/look_for
%attr(0755,root,root) %{_bindir}/slowscan
%attr(0755,root,root) %{_bindir}/watcher
%{perl_vendorlib}/Argus.pm
%{perl_vendorlib}/Argus/Archive.pm
%{perl_vendorlib}/Argus/SlowScan.pm
%{perl_vendorlib}/Argus/Support.pm
%{perl_vendorlib}/Argus/Watcher.pm
%{perl_vendorlib}/ra.conf
%{_mandir}/man1/slowscan.1*
%{_mandir}/man1/watcher.1*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0:2.00-6mdv2011.0
+ Revision: 680475
- mass rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0:2.00-5mdv2011.0
+ Revision: 430260
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0:2.00-4mdv2009.0
+ Revision: 241149
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 01 2007 David Walluck <walluck@mandriva.org> 0:2.00-2mdv2008.0
+ Revision: 20217
- provide perl(Argus::Support) to fill dependency


* Wed Oct 25 2006 David Walluck <walluck@mandriva.org> 2.00-1mdv2007.0
+ Revision: 72201
- BuildRequires: perl-DateManip
- fix all rpmlint warnings
- Import perl-Argus

* Sun Oct 22 2006 David Walluck <walluck@mandriva.org> 0:2.00-1mdv2007.1
- release


