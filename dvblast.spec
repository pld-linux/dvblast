Summary:	DVB/ASI network streamer
Summary(pl.UTF-8):	Aplikacja do tworzenia strumieni sieciowych DVB/ASI
Name:		dvblast
Version:	2.1.0
Release:	1
License:	GPL v2+
Group:		Networking
Source0:	http://downloads.videolan.org/dvblast/2.1/%{name}-%{version}.tar.bz2
# Source0-md5:	df2287811abf2bbc0f8efdcc9f446192
URL:		http://www.videolan.org/projects/dvblast.html
BuildRequires:	bitstream
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DVBlast is a simple and powerful MPEG-2/TS demux and streaming
application with several input methods:
 - Linux-supported DVB cards (DVB-S, DVB-S2, DVB-C, DVB-T...)
 - DVB-ASI cards
 - UDP or RTP stream carrying a transport stream

It outputs one or several RTP streams carrying transport streams with:
 - hardware or software PID filtering
 - PID-based or service-based demultiplexing
 - optional descrambling via CAM device
 - optional DVB tables

%description -l pl.UTF-8
DVBlast to prosta, ale mająca duże możliwości aplikacja
demultipleksująca MPEG-2/TS oraz generująca strumienie, mająca kilka
metod wejściowych:
 - karty DVB obsługiwane przez Linuksa (DVB-S, DVB-S3, DVB-C,
   DVB-T...)
 - karty DVB-ASI
 - strumienie UDP lub RTP niosące strumień transportowy

Wyjściem może być jeden lub kilka strumieni RTP niosących strumienie
transportowe z:
 - sprzętowym lub programowym filtrowaniem PID-ów
 - demultipleksowaniem w oparciu o PID-y lub usługi
 - opcjonalnym rozszyfrowywaniem poprzez urządzenie CAM
 - opcjonalnymi tablicami DVB

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
%{__make} \
	CC="%{__cc}" \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}*
%{_mandir}/man1/%{name}.1*
