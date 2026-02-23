% ══════════════════════════════════════════════════════════════
% wilson-report.cls — Wilson's Multi-Asset Research document class
% Usage: \documentclass{wilson-report}
% Compile with: xelatex (two passes for page references)
% ══════════════════════════════════════════════════════════════

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{wilson-report}[2026/02/23 Wilson's Multi-Asset Research]

\LoadClass[11pt,a4paper]{article}

% ── Fonts (XeLaTeX) ──
\RequirePackage{fontspec}
\setmainfont{Latin Modern Roman}
\setsansfont{Latin Modern Sans}
\setmonofont{Latin Modern Mono}

% ── Page Layout ──
\RequirePackage[
  top=2.0cm, bottom=2.0cm, left=2.2cm, right=2.2cm,
  headheight=45pt, headsep=12pt, footskip=30pt
]{geometry}

% ── Colours ──
\RequirePackage[dvipsnames,svgnames,x11names]{xcolor}
\definecolor{BrandNavy}{HTML}{1B2A4A}
\definecolor{BrandAccent}{HTML}{2E86AB}
\definecolor{BrandGold}{HTML}{D4A843}
\definecolor{BrandLightGrey}{HTML}{F2F4F7}
\definecolor{BrandMidGrey}{HTML}{6B7280}
\definecolor{BrandDarkText}{HTML}{1F2937}
\definecolor{BullGreen}{HTML}{059669}
\definecolor{BearRed}{HTML}{DC2626}
\definecolor{NeutralAmber}{HTML}{D97706}
\definecolor{StaleWarning}{HTML}{B45309}

% ── Tables ──
\RequirePackage{booktabs}
\RequirePackage{tabularx}
\RequirePackage{colortbl}
\RequirePackage{multirow}
\RequirePackage{array}
\renewcommand\tabularxcolumn[1]{>{\raggedright\arraybackslash}m{#1}}

% ── Typography & Spacing ──
\RequirePackage{parskip}
\RequirePackage{enumitem}
\RequirePackage{titlesec}

% ── Header / Footer ──
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}

% ── Misc ──
\RequirePackage{graphicx}
\RequirePackage{hyperref}
\RequirePackage{tikz}
\RequirePackage{amssymb}
\RequirePackage{float}

% ── Hyperlinks (defaults — override pdftitle etc. in each report) ──
\hypersetup{
  colorlinks=true,
  linkcolor=BrandNavy,
  urlcolor=BrandAccent,
  citecolor=BrandNavy,
  pdfauthor={Wilson's Multi-Asset Research}
}

% ── Section Formatting ──
\RequirePackage{needspace}

\titleformat{\section}
  {\needspace{5\baselineskip}\Large\bfseries\color{BrandNavy}}
  {\thesection.}{0.5em}{}
  [\vspace{-0.5em}{\color{BrandAccent}\rule{\textwidth}{1.5pt}}]

\titleformat{\subsection}
  {\needspace{4\baselineskip}\large\bfseries\color{BrandNavy}}
  {\thesubsection}{0.5em}{}

\titleformat{\subsubsection}
  {\needspace{3\baselineskip}\normalsize\bfseries\color{BrandDarkText}}
  {\thesubsubsection}{0.5em}{}

% ── Header / Footer Style ──
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyhead[L]{\small\color{BrandMidGrey}\textbf{WILSON'S MULTI-ASSET RESEARCH}}
\fancyhead[R]{\small\color{BrandMidGrey}\today}
\fancyfoot[C]{\small\color{BrandMidGrey}Page \thepage\ of \pageref{LastPage}}

% ══════════════════════════════════════════
% CUSTOM COMMANDS
% ══════════════════════════════════════════

% Executive summary box
\newcommand{\execsummary}[1]{%
  \begin{tikzpicture}
    \node[fill=BrandLightGrey, rounded corners=4pt, inner sep=12pt,
      text width=\textwidth-24pt, draw=BrandAccent, line width=1pt
    ] {{\large\bfseries\color{BrandNavy}Executive Summary}\par\vspace{6pt} #1};
  \end{tikzpicture}\vspace{0.5em}}

% Conviction badge: \conviction{H}, \conviction{M}, \conviction{L}
\newcommand{\conviction}[1]{%
  \ifx#1H\colorbox{BullGreen}{\color{white}\small\bfseries\,HIGH\,}%
  \else\ifx#1M\colorbox{NeutralAmber}{\color{white}\small\bfseries\,MEDIUM\,}%
  \else\ifx#1L\colorbox{BrandMidGrey}{\color{white}\small\bfseries\,LOW\,}%
  \fi\fi\fi}

% Direction badges
\newcommand{\overweight}{\colorbox{BullGreen}{\color{white}\small\bfseries\,OVERWEIGHT\,}}
\newcommand{\underweight}{\colorbox{BearRed}{\color{white}\small\bfseries\,UNDERWEIGHT\,}}
\newcommand{\neutralweight}{\colorbox{NeutralAmber}{\color{white}\small\bfseries\,NEUTRAL\,}}

% Stale data warning
\newcommand{\staledata}[1]{%
  {\color{StaleWarning}\small$\triangle$ \textit{Data as of #1 --- may not reflect current conditions.}}}

% Key insight callout box
\newcommand{\keyinsight}[1]{%
  \begin{tikzpicture}
    \node[fill=BrandNavy, rounded corners=3pt, inner sep=10pt,
      text width=\textwidth-20pt
    ] {{\color{BrandGold}\bfseries KEY INSIGHT}\par\vspace{4pt}{\color{white}#1}};
  \end{tikzpicture}\vspace{0.5em}}

% Scenario table row colours
\newcommand{\bullrow}{\rowcolor{BullGreen!10}}
\newcommand{\baserow}{\rowcolor{BrandLightGrey}}
\newcommand{\bearrow}{\rowcolor{BearRed!10}}

% AI hypothesis flag
\newcommand{\aihypothesis}[1]{%
  \begin{tikzpicture}
    \node[fill=BrandLightGrey, rounded corners=3pt, inner sep=10pt,
      text width=\textwidth-20pt, draw=BrandMidGrey, line width=0.5pt, dashed
    ] {{\color{BrandMidGrey}\bfseries\small AI-GENERATED HYPOTHESIS}\par\vspace{4pt}{\color{BrandDarkText}#1}};
  \end{tikzpicture}\vspace{0.5em}}

% Report sign-off
\newcommand{\signoff}{%
  \vfill
  \begin{center}
    {\color{BrandMidGrey}\rule{3cm}{0.5pt}}\\[6pt]
    {\small\color{BrandMidGrey}\textbf{Wilson's Multi-Asset Research}}
  \end{center}}

% ══════════════════════════════════════════
% TITLE PAGE
% ══════════════════════════════════════════
% \maketitlepage{Title}{Classification}{Asset Classes}{Horizon}
\newcommand{\maketitlepage}[4]{%
  \thispagestyle{empty}
  \begin{tikzpicture}[remember picture, overlay]
    \fill[BrandNavy] (current page.north west) rectangle ([yshift=-7.75cm]current page.north east);
    \fill[BrandAccent] ([yshift=-7.75cm]current page.north west) rectangle ([yshift=-7.9cm]current page.north east);
    \fill[BrandGold] ([yshift=-7.9cm]current page.north west) rectangle ([yshift=-8.0cm]current page.north east);
  \end{tikzpicture}
  \vspace*{-1.5cm}
  \begin{flushleft}
    {\color{white}\small\textbf{WILSON'S MULTI-ASSET RESEARCH}}\\[0.4cm]
    {\color{white}\Huge\bfseries #1}\\[0.5cm]
    {\color{BrandGold}\large\bfseries #2}\\[0.3cm]
    {\color{white}\normalsize #3 \hfill #4}\\[0.2cm]
    {\color{BrandAccent}\normalsize\today}
  \end{flushleft}
  \vspace{1.0cm}}

\endinput
