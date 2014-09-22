%global cartridgedir %{_libexecdir}/openshift/cartridges/monit

Summary:       Embedded monit support for OpenShift
Name:          openshift-origin-cartridge-monit
Version:       1.0.6
Release:       1%{?dist}
Group:         Network/Daemons
License:       CeCILL

URL:           http://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz

Requires:      monit
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util

BuildArch:     noarch

%description
Provides monit cartridge support to OpenShift

%prep
%setup -q

%build
%__rm %{name}.spec
%__rm -rf rel-eng

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%post
# To modify an alternative you should:
# - remove the previous version if it's no longer valid
# - install the new version with an increased priority
# - set the new version as the default to be safe


%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/conf/
%attr(0755,-,-) %{cartridgedir}/metadata/
%doc %{cartridgedir}/README.md

%changelog
* Mon Sep 22 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.6-1
- Up manifest file (nicolas.messin@worldline.com)

* Mon Sep 22 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.5-1
- Up manifest file (nicolas.messin@worldline.com)

* Mon Sep 22 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.4-1
- Up install file (nicolas.messin@worldline.com)

* Mon Sep 22 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.3-1
- Up install file

* Fri Sep 19 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.2-1
- Delete bin/install file (nicolas.messin@worldline.com)

* Thu Sep 18 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.1-1
- new package built with tito

* Wed Sep 18 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.O
- Creation of initial monit cartridge 

