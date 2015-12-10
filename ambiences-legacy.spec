Summary: SailfishOS v1.x ambiences removed from v2.x
Name: ambiences-legacy
BuildArch: noarch
Version: 0.0.1
Release: 1
Group: System/GUI/Other
License: TBD


Provides: ambiences-legacy = 0.0.1-1
Requires: ambienced


%description
Contains the SailfishOS v1.x ambiences removed from v2.x:
babyflower camera grassroot moonship oldphone redtrain rope shadeofviolin storm
And the original "Snow White" from before its update, renamed "White Snow" for parallel installation


%files
%defattr(-, root, root)
/usr/share/ambience/*/*.ambience
/usr/share/ambience/*/images/*.jpg
/usr/share/translations/*.qm


%prep
exit 0

%build
exit 0

%install
exit 0

%clean
exit 0


