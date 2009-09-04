%define argus_version 2.0.6.fixes.1

Name:           perl-Argus
Version:        2.00
Release:        %mkrel 5
Epoch:          0
Summary:        Client tools for argus network audit
License:        GPL
Group:          Development/Perl
Url:            http://qosient.com/argus/
Source0:        ftp://ftp.qosient.com/dev/argus-2.0/argus-clients-%{argus_version}.tar.bz2
BuildRequires:  perl-DateManip
Provides:       perl(Argus::Support)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Clients to the argus probe which process and display information.

%prep
%setup -q -n argus-clients-%{argus_version}/contrib/Argus-perl-%{version}
export ARGUSHOME=%{_prefix}
%{__perl} Makefile.PL PREFIX=%{_prefix} INSTALLSITELIB=%{perl_vendorlib}
%{__perl} -pi -e 's|local/||g' Makefile

%build
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} -f %{buildroot}%{_prefix}/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

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


