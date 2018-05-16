#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-colourpicker
Version  : 1.0
Release  : 9
URL      : https://cran.r-project.org/src/contrib/colourpicker_1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/colourpicker_1.0.tar.gz
Summary  : A Colour Picker Tool for Shiny and for Selecting Colours in
Group    : Development/Tools
License  : MIT
Requires: R-ggplot2
Requires: R-htmlwidgets
Requires: R-miniUI
Requires: R-shiny
Requires: R-shinyjs
BuildRequires : R-ggplot2
BuildRequires : R-htmlwidgets
BuildRequires : R-miniUI
BuildRequires : R-shiny
BuildRequires : R-shinyjs
BuildRequires : clr-R-helpers

%description
or Rmarkdown documents. The colour picker supports alpha opacity, custom
    colour palettes, and many more options. A Plot Colour Helper tool is
    available as an RStudio Addin, which helps you pick colours to use in your
    plots. A more generic Colour Picker RStudio Addin is also provided to let 
    you select colours to use in your R code.

%prep
%setup -q -c -n colourpicker

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523295587

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523295587
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library colourpicker
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library colourpicker
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library colourpicker
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library colourpicker|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/colourpicker/DESCRIPTION
/usr/lib64/R/library/colourpicker/INDEX
/usr/lib64/R/library/colourpicker/LICENSE
/usr/lib64/R/library/colourpicker/Meta/Rd.rds
/usr/lib64/R/library/colourpicker/Meta/features.rds
/usr/lib64/R/library/colourpicker/Meta/hsearch.rds
/usr/lib64/R/library/colourpicker/Meta/links.rds
/usr/lib64/R/library/colourpicker/Meta/nsInfo.rds
/usr/lib64/R/library/colourpicker/Meta/package.rds
/usr/lib64/R/library/colourpicker/Meta/vignette.rds
/usr/lib64/R/library/colourpicker/NAMESPACE
/usr/lib64/R/library/colourpicker/NEWS.md
/usr/lib64/R/library/colourpicker/R/colourpicker
/usr/lib64/R/library/colourpicker/R/colourpicker.rdb
/usr/lib64/R/library/colourpicker/R/colourpicker.rdx
/usr/lib64/R/library/colourpicker/doc/colourpicker.R
/usr/lib64/R/library/colourpicker/doc/colourpicker.Rmd
/usr/lib64/R/library/colourpicker/doc/colourpicker.html
/usr/lib64/R/library/colourpicker/doc/index.html
/usr/lib64/R/library/colourpicker/examples/colourInput/app.R
/usr/lib64/R/library/colourpicker/examples/colourInput/www/app.css
/usr/lib64/R/library/colourpicker/examples/colourInput/www/github-gray-right.png
/usr/lib64/R/library/colourpicker/examples/colourInput/www/salvattore.min.js
/usr/lib64/R/library/colourpicker/gadgets/colourpicker/css/app.css
/usr/lib64/R/library/colourpicker/gadgets/colourpicker/css/plotHelper.css
/usr/lib64/R/library/colourpicker/gadgets/colourpicker/img/ajax-loader.gif
/usr/lib64/R/library/colourpicker/gadgets/colourpicker/js/shinyjs-funcs.js
/usr/lib64/R/library/colourpicker/help/AnIndex
/usr/lib64/R/library/colourpicker/help/aliases.rds
/usr/lib64/R/library/colourpicker/help/colourpicker.rdb
/usr/lib64/R/library/colourpicker/help/colourpicker.rdx
/usr/lib64/R/library/colourpicker/help/paths.rds
/usr/lib64/R/library/colourpicker/html/00Index.html
/usr/lib64/R/library/colourpicker/html/R.css
/usr/lib64/R/library/colourpicker/htmlwidgets/colourWidget.js
/usr/lib64/R/library/colourpicker/htmlwidgets/colourWidget.yaml
/usr/lib64/R/library/colourpicker/htmlwidgets/lib/jquery/jquery.min.js
/usr/lib64/R/library/colourpicker/img/allowTransparent.png
/usr/lib64/R/library/colourpicker/img/colourPickerGadget.gif
/usr/lib64/R/library/colourpicker/img/colourinput.png
/usr/lib64/R/library/colourpicker/img/colourinputnew.PNG
/usr/lib64/R/library/colourpicker/img/colourpickerscrnshot.png
/usr/lib64/R/library/colourpicker/img/limited-palette.png
/usr/lib64/R/library/colourpicker/img/plothelper-demo.gif
/usr/lib64/R/library/colourpicker/img/plothelper-demo.png
/usr/lib64/R/library/colourpicker/img/showColour.png
/usr/lib64/R/library/colourpicker/rstudio/addins.dcf
/usr/lib64/R/library/colourpicker/srcjs/input_binding_colour.js
/usr/lib64/R/library/colourpicker/www/shared/colourpicker/css/colourpicker.css
/usr/lib64/R/library/colourpicker/www/shared/colourpicker/css/colourpicker.min.css
/usr/lib64/R/library/colourpicker/www/shared/colourpicker/js/colourpicker.js
/usr/lib64/R/library/colourpicker/www/shared/colourpicker/js/colourpicker.min.js
