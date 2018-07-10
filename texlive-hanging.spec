# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/hanging
# catalog-date 2009-11-02 14:28:41 +0100
# catalog-license lppl1.3
# catalog-version 1.2b
Name:		texlive-hanging
Version:	1.2b
Release:	11
Summary:	Hanging paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hanging
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hanging.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hanging.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hanging.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The hanging package facilitates the typesetting of hanging
paragraphs. The package also enables typesetting with hanging
punctuation, by making punctuation characters active. This
facility is best suppressed (it can interfere with other
packages) -- there are package options for suppressing each
individual punctuation character. 'Real' attempts at hanging
punction should nowadays use the microtype package, which takes
advantage of the support offered in recent versions of pdfTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hanging/hanging.sty
%doc %{_texmfdistdir}/doc/latex/hanging/README
%doc %{_texmfdistdir}/doc/latex/hanging/hanging.pdf
#- source
%doc %{_texmfdistdir}/source/latex/hanging/hanging.dtx
%doc %{_texmfdistdir}/source/latex/hanging/hanging.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2b-2
+ Revision: 752459
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2b-1
+ Revision: 718597
- texlive-hanging
- texlive-hanging
- texlive-hanging
- texlive-hanging

