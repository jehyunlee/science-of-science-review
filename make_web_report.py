# -*- coding: utf-8 -*-
"""Science of Science 서베이 보고서 - Web HTML 생성기"""
import os, base64

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(BASE_DIR, '..', 'fig_images')
OUT_FILE = os.path.join(BASE_DIR, 'index.html')

def img_b64(filename):
    path = os.path.join(FIG_DIR, filename)
    if not os.path.exists(path):
        return None
    with open(path, 'rb') as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    ext = filename.rsplit('.', 1)[-1].lower()
    mime = {'png':'image/png','jpg':'image/jpeg','jpeg':'image/jpeg'}.get(ext,'image/png')
    return f'data:{mime};base64,{data}'

def img_tag(filename, alt='', cls='', style=''):
    src = img_b64(filename)
    if src is None:
        return f'<div class="img-placeholder">[이미지: {filename}]</div>'
    attrs = f'src="{src}" alt="{alt}"'
    if cls: attrs += f' class="{cls}"'
    if style: attrs += f' style="{style}"'
    return f'<img {attrs}>'

def cover_banner(filename, alt=''):
    src = img_b64(filename)
    if src is None:
        return f'<div class="chapter-banner chapter-banner-placeholder"><span>{alt}</span></div>'
    return f'<div class="chapter-banner" style="background-image:url(\'{src}\')"></div>'

def info_box(title, lines):
    items = ''.join(f'<p>{l}</p>' for l in lines)
    return f'<div class="info-box"><div class="box-title">[{title}]</div>{items}</div>'

def challenge_box(title, items):
    li = ''.join(f'<li>{i}</li>' for i in items)
    return f'<div class="challenge-box"><div class="box-title">{title}</div><ul>{li}</ul></div>'

def table_html(headers, rows):
    ths = ''.join(f'<th>{h}</th>' for h in headers)
    trs = ''
    for i, row in enumerate(rows):
        cls = ' class="alt-row"' if i % 2 == 1 else ''
        tds = ''.join(f'<td>{c}</td>' for c in row)
        trs += f'<tr{cls}>{tds}</tr>'
    return f'<div class="table-wrap"><table><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table></div>'

def arrow(text):
    return f'<div class="arrow-summary"><span class="arrow-icon">&#9838;</span> {text}</div>'

def fn(n):
    t = FOOTNOTES.get(n, '')
    safe = t.replace('"', '&quot;')
    return f'<sup class="fn" data-n="{n}" title="{safe}">[{n}]</sup>'

FOOTNOTES = {
    1: 'Price, D. J. de S. (1965). Networks of Scientific Papers. Science, 149(3683), 510-515.',
    2: 'Price, D. J. de S. (1976). A General Theory of Bibliometric and Other Cumulative Advantage Processes. JASIS, 27(5), 292-306.',
    3: 'Fortunato, S. et al. (2018). Science of Science. Science, 359(6379), eaao0185.',
    4: 'Watts, D. J. & Strogatz, S. H. (1998). Collective Dynamics of Small-World Networks. Nature, 393, 440-442.',
    5: 'Newman, M. E. J. (2001). The Structure of Scientific Collaboration Networks. PNAS, 98(2), 404-409.',
    6: 'Barabasi, A.-L. & Albert, R. (1999). Emergence of Scaling in Random Networks. Science, 286(5439), 509-512.',
    7: 'Barabasi, A.-L. et al. (2002). Evolution of the Social Network of Scientific Collaborations. Physica A, 311(3-4), 590-614.',
    8: 'Wuchty, S., Jones, B. F. & Uzzi, B. (2007). The Increasing Dominance of Teams in Production of Knowledge. Science, 316(5827), 1036-1039.',
    9: 'Jones, B. F. (2009). The Burden of Knowledge and the Death of the Renaissance Man. Review of Economic Studies, 76(1), 283-317.',
    10: 'Milojevic, S. (2014). Principles of Scientific Research Team Formation and Evolution. PNAS, 111(11), 3984-3989.',
    11: 'Liu, L. et al. (2018). Hot Streaks in Artistic, Cultural, and Scientific Careers. Nature, 559, 396-399.',
    12: 'Garfield, E. (1972). Citation Analysis as a Tool in Journal Evaluation. Science, 178(4060), 471-479.',
    13: 'Hirsch, J. E. (2005). An Index to Quantify an Individual\'s Scientific Research Output. PNAS, 102(46), 16569-16572.',
    14: 'Egghe, L. (2006). Theory and Practice of the g-index. Scientometrics, 69(1), 131-152. | Hutchins, B. I. et al. (2016). Relative Citation Ratio (RCR). PLOS Biology, 14(9), e1002541.',
    15: 'Funk, R. J. & Owen-Smith, J. (2017). A Dynamic Network Measure of Technological Change. Management Science, 63(3), 791-817.',
    16: 'Park, M. et al. (2023). Papers and Patents Are Becoming Less Disruptive Over Time. Nature, 613, 138-144.',
    17: 'Ke, Q. et al. (2015). Defining and Identifying Sleeping Beauties in Science. PNAS, 112(24), 7426-7431.',
    18: 'Wang, D., Song, C. & Barabasi, A.-L. (2013). Quantifying Long-term Scientific Impact. Science, 342(6154), 127-132.',
    19: 'Nielsen, M. W. & Andersen, J. P. (2021). Global Citation Inequality Is on the Rise. PNAS, 118(7), e2012208118.',
    20: 'Lariviere, V., Haustein, S. & Mongeon, P. (2015). The Oligopoly of Academic Publishers in the Digital Era. PLOS ONE, 10(6), e0127502.',
    21: 'Lariviere, V. et al. (2013). Bibliometrics: Global Gender Disparities in Science. Nature, 504, 211-213.',
    22: 'Bornmann, L. & Mutz, R. (2015). Growth Rates of Modern Science. JASIST, 66(11), 2215-2222. | Ioannidis, J. P. A. et al. (2020). Updated Science-Wide Author Databases. PLOS Biology, 18(10), e3000918.',
    23: 'Radicchi, F., Fortunato, S. & Castellano, C. (2008). Universality of Citation Distributions. PNAS, 105(45), 17268-17272.',
    24: 'Shen, H. & Barabasi, A.-L. (2014). Collective Credit Allocation in Science. PNAS, 111(34), 12325-12330.',
    25: 'Van Eck, N. J. & Waltman, L. (2010). Software Survey: VOSviewer. Scientometrics, 84(2), 523-538.',
    26: 'Borner, K. et al. (2012). Design and Update of a Classification System: The UCSD Map of Science. PLOS ONE, 7(7), e39464.',
    27: 'Boyack, K. W. & Klavans, R. (2010). Co-Citation Analysis, Bibliographic Coupling, and Direct Citation. JASIST, 61(12), 2389-2404.',
    28: 'Fortunato, S. (2010). Community Detection in Graphs. Physics Reports, 486(3-5), 75-174.',
    29: 'Blondel, V. D. et al. (2008). Fast Unfolding of Communities in Large Networks. JSTAT, 2008(10), P10008.',
    30: 'Gerlach, M. et al. (2018). A Network Approach to Topic Models. Science Advances, 4(7), eaaq1360.',
    31: 'Lo, K. et al. (2020). S2ORC: The Semantic Scholar Open Research Corpus. ACL 2020.',
    32: 'Priem, J. et al. (2022). OpenAlex: A Fully-Open Index of Scholarly Works. arXiv:2205.01833. | Piwowar, H. et al. (2018). The State of OA. PeerJ, 6, e4375.',
    33: 'Wu, L., Wang, D. & Evans, J. A. (2019). Large Teams Develop and Small Teams Disrupt Science and Technology. Nature, 566, 378-382.',
    34: 'Uzzi, B. et al. (2013). Atypical Combinations and Scientific Impact. Science, 342(6154), 468-472.',
    35: 'Lin, Y., Frey, C. B. & Wu, L. (2023). Remote Collaboration Fuses Fewer Breakthrough Ideas. Nature, 623, 987-991.',
    36: 'Way, S. F. et al. (2017). The Misleading Narrative of the Canonical Faculty Productivity Trajectory. PNAS, 114(44), E9216-E9223.',
    37: 'Wang, Y. et al. (2019). Early-Career Setback and Future Career Impact. Nature Communications, 10, 4331.',
    38: 'Yin, Y. et al. (2019). Quantifying the Dynamics of Failure Across Science, Startups, and Security. Nature, 575, 190-194.',
    39: 'Way, S. F. et al. (2019). Productivity, Prominence, and the Effects of Academic Environment. PNAS, 116(22), 10729-10733.',
    40: 'Yang, Y. et al. (2022). Gender-Diverse Teams Produce More Novel and Higher-Impact Scientific Ideas. PNAS, 119(36), e2200841119.',
    41: 'Hofstra, B. et al. (2020). The Diversity-Innovation Paradox in Science. PNAS, 117(17), 9284-9291.',
    42: 'AlShebli, B. K., Rahwan, T. & Woon, W. L. (2018). The Preeminence of Ethnic Diversity in Scientific Collaboration. Nature Communications, 9, 5163.',
    43: 'Kozlowski, D. et al. (2022). Intersectional Inequalities in Science. PNAS, 119(2), e2113067119.',
    44: 'Huang, J. et al. (2020). Historical Comparison of Gender Inequality in Scientific Careers. PNAS, 117(9), 4609-4616.',
    45: 'Sekara, V. et al. (2018). The Chaperone Effect in Scientific Publishing. PNAS, 115(50), 12603-12607.',
    46: 'Freeman, R. B. & Huang, W. (2019). Making Gender Diversity Work for Scientific Discovery and Innovation. Nature Human Behaviour, 3, 1040-1041.',
    47: 'Zhao, Z. et al. (2023). Global Patterns of Migration of Scholars with Economic Development. PNAS, 120(4), e2217937120.',
    48: 'Wang, H. et al. (2023). Scientific Discovery in the Age of Artificial Intelligence. Nature, 620, 47-60.',
    49: 'Jumper, J. et al. (2021). Highly Accurate Protein Structure Prediction with AlphaFold. Nature, 596, 583-589.',
    50: 'Merchant, A. et al. (2023). Scaling Deep Learning for Materials Discovery. Nature, 624, 80-85.',
    51: 'Tshitoyan, V. et al. (2019). Unsupervised Word Embeddings Capture Latent Knowledge from Materials Science Literature. Nature, 571, 95-98.',
    52: 'Liang, W. et al. (2025). Scientific Production in the Era of Large Language Models. Science, 389(6732), adw3000.',
    53: 'Sourati, J. et al. (2026). AI Tools Expand Scientists Impact but Contract Science Focus. Nature.',
    54: 'Liu, Z. et al. (2025). SciSciGPT: Advancing Human-AI Collaboration in the Science of Science. Nature Computational Science.',
    55: 'Xu, H. et al. (2025). The Empowerment of Science of Science by Large Language Models. arXiv:2501.16150.',
    56: 'Lu, C. et al. (2024). The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. arXiv:2408.06292.',
    57: 'Boiko, D. A. et al. (2023). Autonomous Chemical Research with Large Language Models. Nature, 624, 570-578.',
    58: 'Bran, A. M. et al. (2024). Augmenting Large Language Models with Chemistry Tools. Nature Machine Intelligence, 6, 525-535.',
    59: 'Gil, Y. et al. (2025). Automating the Practice of Science. PNAS, 122(2), e2401238121.',
    60: 'Skarlinski, M. et al. (2024). Language Agents Achieve Superhuman Synthesis of Scientific Knowledge. Nature Machine Intelligence.',
    61: 'Ioannidis, J. P. A. (2005). Why Most Published Research Findings Are False. PLOS Medicine, 2(8), e124.',
    62: 'Baker, M. (2016). 1,500 Scientists Lift the Lid on Reproducibility. Nature, 533, 452-454.',
    63: 'Open Science Collaboration. (2015). Estimating the Reproducibility of Psychological Science. Science, 349(6251), aac4716.',
    64: 'Camerer, C. F. et al. (2018). Evaluating the Replicability of Social Science Experiments. Nature Human Behaviour, 2, 637-644.',
    65: 'Fang, F. C., Steen, R. G. & Casadevall, A. (2012). Misconduct Accounts for the Majority of Retracted Scientific Publications. PNAS, 109(42), 17028-17033.',
    66: 'Fanelli, D. et al. (2017). Meta-assessment of Bias in Science. PNAS, 114(14), 3714-3719.',
    67: 'Li, D. & Agha, L. (2015). Big Names or Big Ideas. Science, 348(6233), 434-438.',
    68: 'Bol, T. et al. (2018). The Matthew Effect in Science Funding. PNAS, 115(19), 4887-4890.',
    69: 'Roumbanis, L. (2023). Rethink Funding by Putting the Lottery First. Nature Human Behaviour, 7, 1018-1019.',
    70: 'Azoulay, P., Fons-Rosen, C. & Graff Zivin, J. S. (2019). Does Science Advance One Funeral at a Time? American Economic Review, 109(8), 2889-2920.',
    71: 'Azoulay, P., Graff Zivin, J. S. & Wang, J. (2010). Superstar Extinction. Quarterly Journal of Economics, 125(2), 549-589.',
    72: 'Yin, Y. et al. (2021). Coevolution of Policy and Science During the Pandemic. Science, 371(6525), 128-131.',
    73: 'Yin, Y. et al. (2022). Public Use and Public Funding of Science. Nature Human Behaviour, 6, 1397-1410.',
    74: 'Ma, Y. et al. (2018). Principled Discovery of Science Prize Network. PNAS, 115(48), 12135-12140.',
}


# ── CSS ──────────────────────────────────────────────────
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --navy: #1F3864;
  --blue: #2E74B5;
  --light-blue: #EBF5FB;
  --red-bg: #FDF2F2;
  --red-border: #C03939;
  --sidebar-bg: #1a1a2e;
  --sidebar-text: #c8d0e0;
  --sidebar-active: #4fc3f7;
  --text: #2d2d2d;
  --muted: #666;
  --border: #dde4ee;
}

body {
  font-family: 'Noto Sans KR', 'Pretendard', sans-serif;
  font-size: 15px;
  color: var(--text);
  line-height: 1.75;
  background: #f5f7fa;
  display: flex;
}

/* ── Progress bar ── */
#progress-bar {
  position: fixed; top: 0; left: 0; height: 3px;
  background: linear-gradient(90deg, var(--blue), #4fc3f7);
  width: 0%; z-index: 9999; transition: width 0.1s;
}

/* ── Sidebar ── */
#sidebar {
  width: 280px; min-width: 280px;
  background: var(--sidebar-bg);
  height: 100vh; position: fixed; top: 0; left: 0;
  overflow-y: auto; z-index: 100;
  transition: transform 0.3s;
  display: flex; flex-direction: column;
}

#sidebar-header {
  padding: 24px 20px 16px;
  border-bottom: 1px solid #2e2e4a;
}

#sidebar-header h2 {
  font-size: 13px; font-weight: 700;
  color: #4fc3f7; line-height: 1.4;
  letter-spacing: 0.02em;
}
#sidebar-header p {
  font-size: 11px; color: #888; margin-top: 6px;
}

#toc { padding: 12px 0 24px; flex: 1; }

.toc-chapter {
  padding: 6px 20px 2px;
  font-size: 12px; font-weight: 700;
  color: #7ec8e3; text-transform: uppercase;
  letter-spacing: 0.05em; margin-top: 8px;
}

.toc-section {
  display: block; padding: 5px 20px 5px 28px;
  font-size: 12.5px; color: var(--sidebar-text);
  text-decoration: none; border-left: 3px solid transparent;
  transition: all 0.2s;
}
.toc-section:hover { color: #fff; background: rgba(255,255,255,0.06); }
.toc-section.active {
  color: var(--sidebar-active);
  border-left-color: var(--sidebar-active);
  background: rgba(79,195,247,0.08);
  font-weight: 600;
}

/* hamburger */
#hamburger {
  display: none; position: fixed; top: 14px; left: 14px;
  z-index: 200; background: var(--navy); color: #fff;
  border: none; border-radius: 6px; padding: 8px 12px;
  font-size: 18px; cursor: pointer;
}

/* ── Main content ── */
#main {
  margin-left: 280px;
  max-width: 860px;
  padding: 0 0 60px;
  flex: 1;
}

/* ── Hero cover ── */
#hero {
  height: 420px;
  background-size: cover; background-position: center;
  display: flex; align-items: flex-end;
  background-color: var(--navy);
}

#hero-text {
  background: linear-gradient(0deg, rgba(15,20,50,0.92) 0%, transparent 100%);
  width: 100%; padding: 40px 48px 36px;
}
#hero-text h1 {
  font-size: 28px; font-weight: 700; color: #fff;
  line-height: 1.3;
}
#hero-text p { font-size: 15px; color: #fff; margin-top: 8px; }
#hero-text .date { font-size: 13px; color: #fff; margin-top: 16px; }

/* ── Chapter sections ── */
.chapter {
  background: #fff; margin: 32px 24px;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.07);
  overflow: hidden;
  opacity: 0; transform: translateY(24px);
  transition: opacity 0.5s, transform 0.5s;
}
.chapter.visible { opacity: 1; transform: translateY(0); }

.chapter-banner {
  height: 220px;
  background-size: cover; background-position: center top;
  background-color: var(--navy);
  display: flex; align-items: flex-end;
}
.chapter-banner-placeholder {
  display: flex; align-items: center; justify-content: center;
  background: linear-gradient(135deg, var(--navy), var(--blue));
}
.chapter-banner-placeholder span { color: #fff; font-size: 18px; opacity: 0.6; }

.chapter-body { padding: 36px 44px 40px; }

h1.chapter-title {
  font-size: 22px; font-weight: 700; color: var(--navy);
  margin-bottom: 8px; padding-bottom: 12px;
  border-bottom: 3px solid var(--blue);
}

h2.section-title {
  font-size: 17px; font-weight: 700; color: var(--blue);
  margin: 32px 0 10px; padding-left: 10px;
  border-left: 4px solid var(--blue);
}

h3.sub-title {
  font-size: 15px; font-weight: 700; color: var(--blue);
  margin: 20px 0 8px;
}

p { margin-bottom: 14px; text-align: justify; }

/* ── Info box ── */
.info-box {
  background: var(--light-blue);
  border: 1.5px solid var(--blue);
  border-radius: 8px; padding: 16px 20px;
  margin: 20px 0;
}
.info-box .box-title {
  font-weight: 700; color: var(--navy);
  margin-bottom: 8px; font-size: 14px;
}
.info-box p { margin-bottom: 4px; font-size: 13.5px; }

/* ── Challenge box ── */
.challenge-box {
  background: var(--red-bg);
  border: 1.5px solid var(--red-border);
  border-radius: 8px; padding: 16px 20px;
  margin: 20px 0;
}
.challenge-box .box-title {
  font-weight: 700; color: var(--red-border);
  margin-bottom: 8px; font-size: 14px;
}
.challenge-box ul { padding-left: 18px; }
.challenge-box li { font-size: 13.5px; color: #502020; margin-bottom: 5px; }

/* ── Arrow summary ── */
.arrow-summary {
  background: linear-gradient(90deg, #fff8ee, #fff);
  border-left: 4px solid #e08030;
  padding: 12px 16px; margin: 20px 0;
  border-radius: 0 8px 8px 0;
  font-weight: 600; color: #603010;
  font-size: 14px;
}
.arrow-icon { font-size: 16px; color: #c05028; margin-right: 4px; }

/* ── Tables ── */
.table-wrap { overflow-x: auto; margin: 20px 0; }
table { width: 100%; border-collapse: collapse; font-size: 13px; }
thead tr { background: var(--blue); }
thead th {
  color: #fff; padding: 9px 12px; font-weight: 600;
  text-align: left; white-space: nowrap;
}
tbody td { padding: 8px 12px; border-bottom: 1px solid #dde4ee; }
tr.alt-row td { background: #f2f7fb; }
tbody tr:hover td { background: #e8f0f8; }

/* ── Figures ── */
.figure { text-align: center; margin: 24px 0; }
.figure img { max-width: 100%; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
.figure-caption { font-size: 12.5px; font-weight: 700; color: var(--navy); margin-top: 8px; }
.figure-source { font-size: 11.5px; color: var(--muted); font-style: italic; }
.img-placeholder {
  background: #eef2f8; color: #aaa; padding: 40px;
  text-align: center; border-radius: 8px; font-size: 13px;
}

/* ── Section paper figure ── */
.section-figure {
  margin: 16px 0 24px;
  text-align: center;
}
.section-figure img {
  max-width: 90%;
  max-height: 480px;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.10);
  border: 1px solid #e0e0e0;
}
.section-figure figcaption {
  font-size: 11.5px;
  color: #888;
  margin-top: 8px;
  font-style: italic;
}

/* ── Footnote superscript ── */
.fn {
  color: var(--blue); font-size: 10px; cursor: help;
  font-weight: 600; vertical-align: super;
}

/* ── References ── */
#references { background: #fff; margin: 32px 24px; border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.07); padding: 36px 44px 40px; }
#references h2 { font-size: 20px; font-weight: 700; color: var(--navy);
  margin-bottom: 20px; padding-bottom: 10px; border-bottom: 2px solid var(--blue); }
.ref-item { font-size: 12.5px; color: #333; padding: 5px 0 5px 20px;
  border-bottom: 1px solid #f0f0f0; text-indent: -20px; margin-left: 20px; }
.ref-item a { color: var(--blue); word-break: break-all; }

/* ── Footer ── */
footer { background: var(--navy); color: #aac; padding: 24px 44px;
  font-size: 12px; text-align: center; margin: 0 24px 24px;
  border-radius: 0 0 12px 12px; }

/* ── Print ── */
@media print {
  #sidebar, #progress-bar, #hamburger { display: none !important; }
  #main { margin-left: 0; }
  .chapter { box-shadow: none; opacity: 1; transform: none; }
}

/* ── Responsive ── */
@media (max-width: 768px) {
  #sidebar { transform: translateX(-100%); }
  #sidebar.open { transform: translateX(0); }
  #main { margin-left: 0; }
  #hamburger { display: block; }
  .chapter-body { padding: 20px 18px 24px; }
  #hero-text { padding: 24px 18px 20px; }
  #hero-text h1 { font-size: 20px; }
  #references { margin: 16px 8px; padding: 20px 16px; }
  .chapter { margin: 16px 8px; }
}
"""

# ── TOC data ─────────────────────────────────────────────
TOC_ITEMS = [
    ('cover', '표지 / 개요', []),
    ('ch1', '제1장: SciSci의 탄생과 네트워크 과학 기반', [
        ('ch1-1', '1.1 과학을 과학하다: SciSci의 기원'),
        ('ch1-2', '1.2 소세계 네트워크와 과학 협력의 구조'),
        ('ch1-3', '1.3 척도 없는 네트워크와 허브 과학자'),
        ('ch1-4', '1.4 팀 과학으로의 전환'),
    ]),
    ('ch2', '제2장: 과학 측정의 혁신', [
        ('ch2-1', '2.1 인용 분석의 탄생과 h-지수 혁명'),
        ('ch2-2', '2.2 혁신성 측정: CD 지수와 그 논쟁'),
        ('ch2-3', '2.3 잠자는 숲속의 미녀: 지연된 인정'),
        ('ch2-4', '2.4 인용 불평등과 출판 독과점'),
    ]),
    ('ch3', '제3장: 과학 지식의 구조', [
        ('ch3-1', '3.1 인용 분포의 보편성'),
        ('ch3-2', '3.2 과학 지도 시각화'),
        ('ch3-3', '3.3 커뮤니티 구조와 토픽 모델링'),
        ('ch3-4', '3.4 오픈 데이터 인프라의 혁명'),
    ]),
    ('ch4', '제4장: 과학적 협업과 연구 인력', [
        ('ch4-1', '4.1 팀 규모와 혁신의 역설'),
        ('ch4-2', '4.2 과학 경력의 동역학'),
        ('ch4-3', '4.3 다양성과 과학적 혁신'),
        ('ch4-4', '4.4 멘토십과 샤페론 효과'),
    ]),
    ('ch5', '제5장: AI와 LLM이 바꾸는 SciSci', [
        ('ch5-1', '5.1 AI가 여는 과학적 발견의 새 시대'),
        ('ch5-2', '5.2 LLM과 과학 생산성'),
        ('ch5-3', '5.3 SciSciGPT: AI 기반 과학 측정학'),
        ('ch5-4', '5.4 자율적 과학 에이전트'),
    ]),
    ('ch6', '제6장: 과학 정책, 재현성, 미래', [
        ('ch6-1', '6.1 재현성 위기의 실체'),
        ('ch6-2', '6.2 과학적 부정행위와 편향'),
        ('ch6-3', '6.3 연구비 배분의 과학'),
        ('ch6-4', '6.4 팬데믹과 과학-정책 공진화'),
    ]),
    ('references', '참고문헌', []),
]

def build_toc():
    parts = []
    for (sec_id, title, subs) in TOC_ITEMS:
        parts.append(f'<div class="toc-chapter"><a class="toc-section" href="#{sec_id}">{title}</a></div>')
        for (sub_id, sub_title) in subs:
            parts.append(f'<a class="toc-section" href="#{sub_id}">{sub_title}</a>')
    return '\n'.join(parts)



# ── Chapter content builders ─────────────────────────────

def build_cover_hero():
    src = img_b64('cover_main.png')
    style = f"background-image:url('{src}')" if src else ''
    return f"""
<section id="cover">
<div id="hero" style="{style}">
  <div id="hero-text">
    <h1>Science of Science 서베이 보고서</h1>
    <p>과학을 과학하다: 데이터와 AI로 바라본 과학의 구조, 동역학, 그리고 미래</p>
    <div class="date">2026.02.28.</div>
  </div>
</div>
</section>
"""

def build_ch1():
    return f"""
<section class="chapter" id="ch1">
{cover_banner('cover_ch1.png', '제1장')}
<div class="chapter-body">
<h1 class="chapter-title" id="ch1-top">제1장 &nbsp; SciSci의 탄생과 네트워크 과학 기반</h1>

<h2 class="section-title" id="ch1-1">1.1 &nbsp; 과학을 과학하다: SciSci의 기원</h2>
<p>과학은 자연을 탐구하는 활동이지만, 과학 그 자체도 탐구의 대상이 될 수 있다.
"과학의 과학(Science of Science, SciSci)"이라는 발상은 과학적 방법론을 과학 활동 자체에 적용하려는 시도에서 출발했다.
그 기원은 1960년대로 거슬러 올라간다. 1965년 Derek de Solla Price는 논문 간 인용 관계를 네트워크로
분석한 최초의 연구를 발표했다.{fn(1)}</p>

<p>Price는 인용 네트워크에서 "누적적 이점(cumulative advantage)" 현상을 발견했다.
이미 많이 인용된 논문이 더 많이 인용되는 경향, 즉 "부익부" 메커니즘이 과학 지식의 성장을 지배한다는 것이다.
이 통찰은 1976년 수학적으로 정식화되어, 이후 "선호적 연결(preferential attachment)"이라는
네트워크 과학의 핵심 개념으로 발전했다.{fn(2)}</p>

<p>그로부터 반세기가 지난 2018년, Barabási 등은 Science지에 SciSci 분야의 포괄적 리뷰를 발표하며
이 분야를 체계화했다. 이 리뷰는 논문 생산, 인용 동역학, 협력 패턴, 과학적 영향력의 예측 가능성이라는 네 축을 중심으로
SciSci의 지적 지형을 정리했으며, 컴퓨터 과학·물리학·사회학의 융합이 이 분야의 정체성을 형성하고 있음을 보였다.{fn(3)}</p>

<h2 class="section-title" id="ch1-2">1.2 &nbsp; 소세계 네트워크와 과학 협력의 구조</h2>
<p>과학자들의 협력 관계는 어떤 구조를 이루고 있을까? 이 질문에 답하려면 네트워크 과학의 혁명적 발견을 이해해야 한다.
1998년, Watts와 Strogatz는 규칙적 격자와 완전 무작위 그래프 사이에 존재하는 "소세계(small-world)" 네트워크를 발견했다.
소세계 네트워크에서는 대부분의 노드가 소수의 단계만 거치면 연결되면서도, 동시에 높은 군집 계수를 유지한다.
이 모델은 영화배우 협업 네트워크(평균 3.65 단계), 전력망(18.7 단계), C. elegans 신경망(2.65 단계) 등에서 보편적으로 확인되었다.{fn(4)}</p>

<p>과학 협력 네트워크에도 소세계 속성이 나타났다. Newman은 물리학·생의학·컴퓨터과학 분야의 공저 네트워크를 분석하여,
과학자들이 평균 5-6단계의 분리도를 가지며 높은 군집성을 보임을 확인했다.
특히 생의학 분야의 군집 계수는 0.066으로, 동일 규모의 무작위 네트워크(0.00012)보다 550배 높았다.
이는 과학자들이 강한 지역적 공동체를 형성하면서도 분야 간 "다리" 역할을 하는 소수의 허브 연구자들을 통해 전체가 연결됨을 의미한다.{fn(5)}</p>

<h2 class="section-title" id="ch1-3">1.3 &nbsp; 척도 없는 네트워크와 허브 과학자</h2>
<p>1999년, Barabási와 Albert는 현실 네트워크의 연결 분포가 멱법칙(power law)을 따른다는 사실을 발견했다.
WWW의 페이지 연결도 분포가 P(k) ~ k<sup>-2.1</sup>을 따르며, 대부분의 노드는 소수의 연결만 갖지만
극소수의 "허브"는 수천 개의 연결을 보유한다. 이 "척도 없는(scale-free)" 구조는
"선호적 연결" 메커니즘—새 노드가 이미 연결이 많은 노드에 우선적으로 연결되는 현상—으로 설명되었다.{fn(6)}</p>

<p>과학 협력 네트워크의 진화를 추적한 연구는 이 메커니즘이 학문 세계에서도 작동함을 보여주었다.
수학과 신경과학 분야의 8년간 공저 데이터를 분석한 결과, 새로운 협력 관계가 형성될 때
이미 많은 공저자를 가진 과학자에게 연결될 확률이 비례적으로 높았다.
네트워크는 시간이 지남에 따라 거대 연결 성분(giant component)으로 수렴했으며,
이 거대 성분에 속한 과학자들의 평균 거리는 지속적으로 감소했다.{fn(7)}</p>

<h2 class="section-title" id="ch1-4">1.4 &nbsp; 팀 과학으로의 전환</h2>
<p>네트워크 구조의 이해를 넘어, SciSci의 핵심 발견 중 하나는 과학의 생산 방식 자체가 근본적으로 변화하고 있다는 것이다.
1950년대 이후 과학·공학 전 분야에서 팀 기반 연구의 비중은 꾸준히 증가했다.
450만 편의 논문과 210만 건의 특허를 분석한 결과, 팀 논문의 비율은 과학에서 약 50%에서 80% 이상으로,
공학에서는 60%에서 90% 이상으로 상승했으며, 팀 논문의 평균 인용 횟수는 단독 연구의 2.1배에 달했다.{fn(8)}</p>

<p>팀 과학으로의 전환은 "지식의 부담(burden of knowledge)" 가설과 깊이 연결된다.
과학 지식이 축적될수록 개별 연구자가 전문성을 확보하기까지 필요한 학습 기간이 길어지고,
자연스럽게 협업의 필요성이 증가한다. 미국 특허 데이터 분석에서 첫 특허를 출원하는 평균 연령은
1985년 30.7세에서 2009년 33.7세로 상승했으며, 팀 규모도 동기간 동안 꾸준히 증가했다.{fn(9)}</p>

<p>팀의 규모 분포 자체도 흥미로운 패턴을 보인다.
APS 논문 데이터베이스를 분석한 결과, 팀 규모 분포는 단일 분포가 아닌 두 개의 포아송 분포의 중첩으로 나타났다.
소규모 핵심 팀(2-4명)과 대규모 프로젝트 팀(10명 이상)이라는 두 가지 뚜렷한 협업 모드가 공존하며,
이는 과학 연구에 "탐색형"과 "대규모 검증형"이라는 본질적으로 다른 두 유형이 있음을 시사한다.{fn(10)}</p>

<p>팀의 구조를 넘어, 개인 수준에서도 과학적 성취의 시간적 역학이 밝혀지고 있다.
흥미롭게도 과학적 성취에도 스포츠 선수의 "핫 스트릭"과 유사한 패턴이 존재한다.
수십만 명의 경력 데이터를 분석한 결과, 과학자·영화감독·예술가 모두에서
연속적으로 높은 영향력의 작품을 만들어내는 "핫 스트릭" 기간이 통계적으로 유의하게 나타났다.
이 기간은 무작위가 아니며, 경력 중 언제든 발생할 수 있지만 대부분의 경우 단 한 번 집중적으로 나타났다.{fn(11)}</p>

{table_html(
    ['연도', '발견/개념', '핵심 기여', '주요 연구자'],
    [
        ['1965', '인용 네트워크', '논문 간 인용을 네트워크로 최초 분석', 'Price'],
        ['1976', '누적적 이점', '부익부 현상의 수학적 정식화', 'Price'],
        ['1998', '소세계 네트워크', '높은 군집성 + 짧은 경로 길이의 공존', 'Watts & Strogatz'],
        ['1999', '척도 없는 네트워크', '멱법칙 분포와 선호적 연결 메커니즘', 'Barabási & Albert'],
        ['2001', '공저 네트워크 분석', '과학 협력의 소세계 속성 확인', 'Newman'],
        ['2007', '팀 과학의 부상', '팀 논문 비율 50%→80%, 인용 2.1배', 'Wuchty, Jones, Uzzi'],
        ['2009', '지식의 부담', '전문화 심화와 협업 필요성 증가', 'Jones'],
        ['2018', 'SciSci 체계화', '분야 전체를 포괄하는 종합 리뷰', 'Barabási et al.'],
    ]
)}

{challenge_box('SciSci가 직면한 근본 도전', [
    '데이터 편향: 영어권·고영향력 저널 중심의 데이터는 글로벌 과학 활동의 일부만 포착한다.',
    '인과 추론의 한계: 관찰 데이터에서 인과 관계를 식별하기 어렵다. 협력이 성과를 높이는가, 성과가 높은 사람이 협력하는가?',
    '측정의 환원성: h-지수, 인용 수 등 단일 지표로 과학적 기여의 다면적 가치를 포착할 수 있는가?',
    '재현성: SciSci 자체의 발견도 재현 가능한가? 데이터 시기·범위에 따라 결론이 달라질 수 있다.',
])}

<div class="figure">
{img_tag('fig_ch1.png', '제1장 핵심 그림', 'chapter-fig')}
</div>

{arrow('제1장 요약: 과학은 네트워크 구조를 가지며, 그 생산 방식은 개인에서 팀으로 근본적으로 변화했다. → 이제 이러한 과학 활동을 어떻게 "측정"할 것인가?')}

</div>
</section>
"""


def build_ch2():
    return f"""
<section class="chapter" id="ch2">
{cover_banner('cover_ch2.png', '제2장')}
<div class="chapter-body">
<h1 class="chapter-title" id="ch2-top">제2장 &nbsp; 과학 측정의 혁신</h1>

<h2 class="section-title" id="ch2-1">2.1 &nbsp; 인용 분석의 탄생과 h-지수 혁명</h2>
<p>과학적 영향력을 수치로 측정하려는 시도는 1972년 Eugene Garfield의 선구적 연구에서 시작되었다.
Garfield는 저널 수준에서 인용 빈도를 체계적으로 집계하는 방법론을 제안했으며,
이것이 오늘날 Journal Impact Factor(JIF)의 원형이 되었다.
하나의 저널에 실린 논문이 이후 2년간 평균적으로 받는 인용 수라는 단순한 정의가
학술 출판의 위계 전체를 지배하게 될 줄은 당시 아무도 예상하지 못했다.{fn(12)}</p>

<p>저널 수준의 측정을 넘어 개인 연구자의 영향력을 단일 숫자로 요약하려는 시도는
2005년 물리학자 Jorge Hirsch가 제안한 h-지수에서 결정적 전환점을 맞았다.
h-지수는 "h편의 논문이 각각 h회 이상 인용된" 최대 h값으로 정의된다.
예컨대 h=50인 연구자는 최소 50편의 논문이 각각 50회 이상 인용된 것이다.
이 지표는 단일 대표작의 인용 폭발에 휘둘리지 않으면서도 지속적 기여를 반영한다는 점에서 직관적이었다.{fn(13)}</p>

<p>h-지수의 한계를 보완하려는 시도도 이어졌다. g-지수는 상위 논문의 인용 수를 더 세밀하게 반영한다.
상위 g편 논문의 총 인용 수가 g<sup>2</sup> 이상인 최대 g값으로 정의되며,
고인용 논문이 많은 연구자에게 h-지수보다 높은 값을 부여한다.
분야 간 비교를 가능하게 하려는 시도로 RCR(Relative Citation Ratio)도 등장했다.
NIH가 개발한 이 지표는 같은 분야의 인용 네트워크를 기준으로 정규화하여, 분야 간 인용 관행 차이를 보정한다.{fn(14)}</p>

<h2 class="section-title" id="ch2-2">2.2 &nbsp; 혁신성 측정: CD 지수와 그 논쟁</h2>
<p>인용 횟수가 "얼마나 많이" 주목받았는지를 측정한다면, CD 지수(Consolidation-Disruption index)는
"어떻게" 영향을 미쳤는지를 포착하려는 시도이다.
2017년 Funk와 Owen-Smith가 기술 혁신 맥락에서 제안한 이 지표는,
어떤 논문이 기존 지식을 "공고화(consolidation)"하는지 아니면 "파괴(disruption)"하는지를 -1에서 +1 사이로 수치화한다.
+1에 가까울수록 이전 문헌과의 단절이 크고, -1에 가까울수록 기존 연구의 연장선상에 있다.{fn(15)}</p>

<p>이 지표가 전 세계적 논쟁을 촉발한 것은 2023년 Nature에 발표된 대규모 분석 때문이었다.
4,500만 편의 논문과 390만 건의 특허를 분석한 결과, CD 지수가 1945년부터 2010년까지
전 분야에 걸쳐 급격히 하락했다. 물리학에서 91.9%, 생명과학에서 91.2%의 감소가 관측되었다.
이 결과는 "과학이 점점 덜 파괴적으로 변하고 있다"는 도발적 해석으로 이어졌다.
연구자들이 점점 더 좁은 범위의 선행 연구에 의존하고, 지식의 프런티어가 멀어짐에 따라
진정한 패러다임 전환이 어려워지고 있다는 것이다.{fn(16)}</p>

<h2 class="section-title" id="ch2-3">2.3 &nbsp; 잠자는 숲속의 미녀: 지연된 인정</h2>
<p>과학적 발견이 항상 즉각적으로 인정받는 것은 아니다. "잠자는 미녀(Sleeping Beauty)" 현상은
발표 후 오랫동안 거의 인용되지 않다가 갑자기 "깨어나" 폭발적 인용을 받는 논문을 지칭한다.
Ke 등이 제안한 Beauty coefficient B는 이 현상을 정량화했다. 2,200만 편의 물리학·화학·사회과학 논문을 분석한 결과,
잠자는 미녀는 드물지 않았다. "잠자는 기간"이 수십 년에 달하는 사례가 다수 발견되었으며,
가장 극단적 사례는 117년간 잠자다가 깨어난 물리학 논문이었다.{fn(17)}</p>

<p>과학적 영향력의 장기 역학을 더 정교하게 모델링한 시도도 있다.
Wang, Song, Barabási의 Q-모델은 논문의 인용 궤적을 세 가지 요인으로 분해했다:
논문 고유의 "적합성(fitness)", 발표 시점의 "즉시성(immediacy)", 그리고 시간에 따른 "노화(aging)".
이 모델은 과학적 영향력에서 "운(luck)"과 "실력(fitness)"의 상대적 기여를 정량적으로 분리할 수 있게 해주었다.
흥미롭게도, 논문의 궁극적 인용 수는 적합성보다 초기 인용의 무작위적 변동에 더 민감한 것으로 나타났다.{fn(18)}</p>

<h2 class="section-title" id="ch2-4">2.4 &nbsp; 인용 불평등과 출판 독과점</h2>
<p>과학 측정의 혁신이 가져온 이면에는 깊어지는 불평등이 있다. 인용 분포의 불균등은 시간이 지남에 따라 심화되고 있다.
1980년부터 2020년까지의 데이터를 분석한 결과, 상위 1%의 고인용 논문이 전체 인용의 약 21%를 차지하며,
이 비율은 지난 40년간 증가 추세에 있다. 지니 계수로 측정한 인용 불평등도
대부분의 학문 분야에서 상승했다.{fn(19)}</p>

<p>출판 시장의 구조적 독과점도 과학 생태계의 핵심 과제이다.
Elsevier, Springer Nature, Wiley, Taylor &amp; Francis, SAGE의 5대 출판사가
전체 학술 논문의 약 53%를 출판하며, 특히 사회과학에서는 이 비율이 70%에 달한다.
이러한 집중은 1973-2013년 기간 동안 지속적으로 심화되었으며, 디지털 시대에도 완화되지 않았다.{fn(20)}</p>

<p>출판 시장의 집중이 접근의 불평등을 야기한다면, 연구자 자체의 인구학적 불평등은 더 근본적이다.
성별에 따른 과학 생산성의 격차가 측정을 통해 가시화되었다.
전 세계 논문 데이터를 분석한 결과, 여성 연구자의 비율은 분야에 따라 크게 다르지만
대부분의 분야에서 30% 미만이며, 특히 고인용 논문과 교신저자 비율에서 격차가 두드러졌다.
이러한 격차는 남미와 동유럽에서 상대적으로 작았고, 일본과 사우디아라비아에서 가장 컸다.{fn(21)}</p>

<p>과학의 규모 자체도 전례 없는 속도로 성장하고 있다.
Web of Science 데이터 분석에 따르면, 과학 출판물의 수는 매 15-20년마다 2배로 증가해왔다.
이 지수적 성장은 20세기 초부터 현재까지 놀라울 정도로 일관적이다.
한편, 개인 연구자의 인용 지표를 분야 간 비교할 수 있도록 표준화하려는 노력도 진행 중이며,
700만 명 이상의 연구자를 포함하는 표준화된 인용 데이터베이스가 구축되어 활용되고 있다.{fn(22)}</p>

{table_html(
    ['지표', '제안연도', '측정 대상', '핵심 장점', '주요 한계'],
    [
        ['JIF', '1972', '저널 영향력', '단순하고 직관적', '저널 내 논문 간 편차 무시'],
        ['h-지수', '2005', '개인 생산성+영향력', '생산성과 인용을 동시 반영', '분야 간 비교 불가, 경력 길이 편향'],
        ['g-지수', '2006', '개인 영향력 (상위 집중)', '고인용 논문 가중 반영', 'h-지수보다 복잡, 보급률 낮음'],
        ['CD 지수', '2017', '논문의 혁신성/공고성', '영향력의 "질적" 차원 포착', '계산 복잡, 해석 논쟁 중'],
        ['RCR', '2016', '분야 보정 인용', '분야 간 공정 비교 가능', 'NIH 중심, 인용 네트워크 의존'],
        ['Beauty B', '2015', '지연된 인정', '잠자는 미녀 현상 정량화', '희귀 사건에 최적화, 일반화 한계'],
    ]
)}

{challenge_box('측정의 함정: Goodhart의 법칙과 지표의 왜곡', [
    "Goodhart의 법칙: 측정 지표가 목표가 되면 좋은 측정 지표가 되기를 멈춘다. h-지수 최적화를 위한 자기인용, 상호인용 네트워크가 문제화.",
    '분야 간 비교 불가: 수학(평균 인용 ~5)과 생의학(평균 인용 ~30)을 동일 지표로 비교하면 구조적 불공정 발생.',
    '시간 편향: 최근 논문은 인용 축적 시간이 부족하여 체계적으로 불리. CD 지수의 시계열 감소도 이 편향에 부분적으로 기인할 수 있음.',
    '다면적 가치의 환원: 교육적 기여, 데이터 공유, 소프트웨어 개발, 정책 자문 등 인용으로 포착되지 않는 과학적 기여가 체계적으로 무시됨.',
])}

<div class="figure">
{img_tag('fig_ch2.png', '제2장 핵심 그림', 'chapter-fig')}
</div>

{arrow('제2장 요약: 과학 측정 지표의 발전은 과학 활동의 정량적 이해를 가능하게 했지만, 동시에 지표의 한계와 왜곡도 드러냈다. → 이제 이 지표들로 드러난 과학 지식의 거시적 구조를 살펴보자.')}

</div>
</section>
"""



def build_ch3():
    return f"""
<section class="chapter" id="ch3">
{cover_banner('cover_ch3.png', '제3장')}
<div class="chapter-body">
<h1 class="chapter-title" id="ch3-top">제3장 &nbsp; 과학 지식의 구조</h1>

<h2 class="section-title" id="ch3-1">3.1 &nbsp; 인용 분포의 보편성</h2>
<p>개별 논문의 인용 수는 분야마다 천차만별이지만, 인용 분포의 통계적 형태에는 놀라운 보편성이 존재한다.
물리학·화학·생물학 등 다양한 분야의 인용 데이터를 분석한 결과,
각 분야의 인용 분포를 해당 분야의 평균 인용 수로 정규화하면 모든 분야가 단일 보편 곡선으로 수렴했다.
이는 인용의 절대적 규모는 분야마다 다르지만, 그 이면의 통계적 메커니즘은 동일하다는 것을 의미한다.
소수의 고인용 논문이 전체 인용의 대부분을 차지하는 "멱법칙적" 패턴이 학문 분야를 초월하여 보편적으로 나타난다.{fn(23)}</p>

<p>이러한 보편성은 과학 지식의 성장 메커니즘에 대한 근본적 통찰을 제공한다.
인용 과정에서 "선호적 연결"과 "적합성"이 동시에 작용하며,
논문의 궁극적 운명은 출판 직후의 초기 인용 역학에 의해 상당 부분 결정된다.
한편, 개별 과학자에 대한 공헌 배분도 구조적 패턴을 보인다.
다저자 논문에서 신용(credit)이 어떻게 분배되는지를 분석한 결과,
첫 번째 저자와 마지막 저자(통상 교신저자)가 불균형적으로 많은 신용을 받으며,
중간 저자의 기여는 체계적으로 과소평가되는 것으로 나타났다.{fn(24)}</p>

<h2 class="section-title" id="ch3-2">3.2 &nbsp; 과학 지도 시각화</h2>
<p>과학 지식의 전체 지형을 볼 수 있어야 한다. 수백만 편의 논문이 형성하는 인용 네트워크를 시각적으로 매핑하려는
시도는 과학의 거시적 구조를 드러낸다. VOSviewer는 이러한 시각화 도구의 대표적 사례로,
공인용(co-citation) 분석, 서지 결합(bibliographic coupling), 키워드 공출현 분석 등을 통해
연구 분야 간 관계를 2차원 지도로 표현한다. 출시 이후 누적 200만 회 이상 다운로드되며
과학 매핑의 사실상 표준 도구로 자리잡았다.{fn(25)}</p>

<p>VOSviewer가 드러낸 전체 지형을 더 체계적으로 분류하려는 시도도 이어졌다.
UCSD 과학 지도 프로젝트는 Scopus와 Web of Science의 2,500만 편 이상의 논문 데이터를 기반으로
554개의 학문 하위 분야를 13개 주요 클러스터로 매핑했다.
이 지도에서 물리학과 수학은 서로 인접하고, 사회과학과 의학은 별도의 대륙을 형성하며,
컴퓨터과학은 공학과 수학 사이의 "다리" 역할을 한다.{fn(26)}</p>

<p>지형을 보여준다면 읽어내는 것은 또 다른 과제이다.
공인용과 직접 인용, 서지 결합이라는 세 가지 접근법을 비교한 연구에 따르면,
연구 프런티어를 가장 정확하게 포착하는 것은 직접 인용 방식이었다.
공인용 분석은 과거의 확립된 구조를, 서지 결합은 현재의 활발한 연구 영역을 더 잘 반영했다.
이 세 방법의 조합이 과학 구조의 시간적 변화를 입체적으로 이해하는 데 필수적이다.{fn(27)}</p>

<h2 class="section-title" id="ch3-3">3.3 &nbsp; 커뮤니티 구조와 토픽 모델링</h2>
<p>과학 지식 네트워크의 구조를 이해하는 또 다른 접근은 커뮤니티 탐지(community detection)이다.
복잡계 네트워크에서 커뮤니티란 내부 연결이 외부 연결보다 밀도가 높은 노드 그룹을 뜻한다.
Fortunato의 포괄적 리뷰는 모듈성(modularity) 최적화, 스펙트럼 방법, 레이블 전파 등
수십 가지 알고리즘을 체계적으로 비교 분석했으며, 이 리뷰 자체가 1만 회 이상 인용되어
네트워크 과학에서 가장 영향력 있는 논문 중 하나가 되었다.{fn(28)}</p>

<p>대규모 네트워크에서 실용적으로 사용할 수 있는 커뮤니티 탐지 알고리즘의 대표적 사례가
Louvain 방법이다. 이 알고리즘은 모듈성을 탐욕적으로(greedily) 최적화하면서
계층적으로 커뮤니티를 병합하는 다단계 접근법을 사용한다.
계산 복잡도가 O(n log n)으로 매우 효율적이어서 수백만 노드의 네트워크도 처리할 수 있으며,
인용 네트워크, 공저 네트워크, 소셜 네트워크 등 다양한 도메인에서 사실상의 표준으로 사용된다.{fn(29)}</p>

<p>네트워크 구조 분석과 자연어 처리를 결합한 새로운 접근법도 등장했다.
인용 네트워크 위에 토픽 모델(topic model)을 결합하면 논문의 주제적 유사성과 인용 관계를
동시에 고려할 수 있다. 이 네트워크 기반 토픽 모델은 전통적인 LDA보다
과학 분야의 진화를 더 정확하게 추적할 수 있었으며, 특히 학제 간 연구의 흐름을 포착하는 데 강점을 보였다.{fn(30)}</p>

<h2 class="section-title" id="ch3-4">3.4 &nbsp; 오픈 데이터 인프라의 혁명</h2>
<p>과학 지식 구조의 분석은 데이터 인프라의 발전 없이는 불가능하다.
2020년에 공개된 S2ORC(Semantic Scholar Open Research Corpus)는
8,100만 편 이상의 학술 논문에 대한 전문 텍스트, 메타데이터, 인용 관계를 포함하는
대규모 오픈 데이터셋이다. 이는 자연어 처리와 과학 측정학의 교차점에서
새로운 연구를 가능하게 한 핵심 인프라가 되었다.{fn(31)}</p>

<p>더 야심적인 시도로, OpenAlex는 Microsoft Academic Graph의 후속 프로젝트로서
2억 편 이상의 학술 저작물, 6천만 명의 연구자, 10만 개의 출처를 포괄하는 완전 오픈 인덱스이다.
기존의 상업적 데이터베이스(Web of Science, Scopus)와 달리 무료로 접근할 수 있으며,
API와 데이터 스냅샷을 통해 대규모 과학 측정학 연구의 민주화에 기여하고 있다.
오픈 액세스(OA)의 확산도 이러한 변화의 일부이다. 2018년 기준 전체 논문의 약 28%가 어떤 형태로든
OA로 제공되고 있으며, Green OA(저자 자체 아카이빙)가 가장 큰 비중을 차지했다.{fn(32)}</p>

{table_html(
    ['데이터 인프라', '공개연도', '규모', '특징', '접근성'],
    [
        ['Web of Science', '1964', '~2억 건', '가장 오랜 역사, 엄격한 저널 선별', '상업적 (유료)'],
        ['Scopus', '2004', '~2.5억 건', '넓은 커버리지, Elsevier 운영', '상업적 (유료)'],
        ['S2ORC', '2020', '8,100만+', '전문 텍스트 포함, NLP 연구 최적화', '오픈 (무료)'],
        ['OpenAlex', '2022', '2억+', 'MAG 후속, 완전 오픈, API 제공', '오픈 (무료)'],
        ['VOSviewer', '2010', 'N/A', '시각화 도구, 200만+ 다운로드', '오픈 (무료)'],
    ]
)}

{challenge_box('과학 지식 구조 분석의 도전', [
    '데이터 완전성: 어떤 단일 데이터베이스도 전체 과학 출판물을 포괄하지 못한다. 비영어권, 사회과학, 인문학의 누락이 체계적.',
    '동적 분류의 어려움: 학문 분야의 경계는 고정되어 있지 않다. 새로운 학제 간 분야의 등장을 기존 분류 체계가 따라가지 못함.',
    '인용 시차와 편향: 인용에는 시간이 걸리며, 방법론 논문이 실질적 발견 논문보다 더 많이 인용되는 구조적 편향이 존재.',
    '스케일의 저주: 수억 편의 논문 데이터를 처리하려면 계산 비용이 막대하며, 실시간 분석은 여전히 도전적.',
])}

<div class="figure">
{img_tag('fig_ch3.png', '제3장 핵심 그림', 'chapter-fig')}
</div>

{arrow('제3장 요약: 과학 지식은 보편적 통계 법칙을 따르는 네트워크 구조를 가지며, 오픈 데이터 인프라가 이 구조의 분석을 민주화하고 있다. → 이 구조 안에서 과학자들은 어떻게 협업하고, 경력을 쌓는가?')}

</div>
</section>
"""


def build_ch4():
    return f"""
<section class="chapter" id="ch4">
{cover_banner('cover_ch4.png', '제4장')}
<div class="chapter-body">
<h1 class="chapter-title" id="ch4-top">제4장 &nbsp; 과학적 협업과 연구 인력</h1>

<h2 class="section-title" id="ch4-1">4.1 &nbsp; 팀 규모와 혁신의 역설</h2>
<p>팀 과학이 지배적이 된 시대에, 팀의 크기는 연구의 성격에 어떤 영향을 미치는가?
이 질문에 대한 답은 놀라운 역설을 드러냈다. 6,500만 편의 논문, 특허, 소프트웨어 프로젝트를 분석한 결과,
대규모 팀은 기존 아이디어를 발전·정교화하는 반면, 소규모 팀(1-3명)이 과학과 기술의 방향을
"파괴적으로(disruptively)" 전환하는 경향이 강했다.
CD 지수로 측정한 파괴성은 팀 규모가 커질수록 단조롭게 감소했다.{fn(33)}</p>

<p>비전통적 아이디어의 조합도 팀의 창의성에 핵심적 역할을 한다.
1,790만 편의 논문을 분석한 결과, "전형적" 인용 조합과 "비전형적" 인용 조합을 동시에 포함하는 논문이
가장 높은 인용 영향력을 보였다. 관습적 지식과 참신한 조합을 모두 갖춘 연구가
순수한 참신함이나 순수한 관습보다 과학적 영향력이 높다는 것이다.
특히 팀 연구가 이러한 "비전형적 조합"을 생산하는 데 단독 연구보다 유리했다.{fn(34)}</p>

<p>원격 협업의 증가가 이 역학을 어떻게 변화시키고 있는지도 중요한 질문이다.
코로나19 이후 폭발적으로 증가한 원격 협업의 효과를 2,000만 편의 논문과 400만 건의 특허로 분석한 결과,
같은 건물에서 일하는 연구자들의 논문이 원격 협업 논문보다 파괴적 혁신(CD 지수 기준)에서 유의하게 높았다.
물리적 근접성이 비정형적 아이디어 교환을 촉진하며, 화상회의와 이메일만으로는
이를 완전히 대체할 수 없다는 것이다.{fn(35)}</p>

<h2 class="section-title" id="ch4-2">4.2 &nbsp; 과학 경력의 동역학</h2>
<p>과학자의 경력은 어떤 패턴을 따르는가? "정전적(canonical)" 생산성 궤적—젊은 시절 생산성이 정점을 찍고
이후 감소한다는 통념—은 실제 데이터와 부합하지 않는다.
미국 대학 교수진의 생산성 데이터를 분석한 결과, 이 통념적 궤적은
개인 수준에서는 거의 관찰되지 않았다. 대부분의 연구자는 경력 전반에 걸쳐
상당히 일정한 생산성을 유지하거나, 후기에 오히려 증가하는 패턴을 보였다.{fn(36)}</p>

<p>경력 초기의 좌절이 장기적 성과에 미치는 영향도 흥미로운 발견이다.
NIH R01 연구비 심사에서 아슬아슬하게 탈락한 "근소 실패(near-miss)" 연구자들을
간신히 통과한 "근소 성공(near-win)" 연구자들과 비교한 결과,
초기 좌절을 경험한 그룹이 이후 10년간 오히려 더 높은 인용 영향력을 보였다.
이 역설적 결과는 초기 실패가 일종의 선별 효과(약한 연구자의 이탈)와 동기 부여 효과를 가질 수 있음을 시사한다.{fn(37)}</p>

<p>실패의 동역학은 과학에만 국한되지 않는다. 과학 연구비 신청, 스타트업 투자, 테러 공격 등
다양한 도메인의 실패 패턴을 분석한 결과, "성공적 실패"와 "영구적 실패"를 구분하는 핵심 요인이 밝혀졌다.
궁극적으로 성공하는 그룹은 매 시도마다 조금씩 개선되는 반면, 실패를 반복하는 그룹은
시도 간에 유의미한 학습이 관찰되지 않았다. 성공과 실패의 분기점은 "시도 횟수"가 아니라 "시도 간 학습률"이었다.{fn(38)}</p>

<p>학문적 환경 자체가 연구자의 생산성에 미치는 영향도 무시할 수 없다.
미국 컴퓨터과학 교수진의 이동 데이터를 분석한 결과, 연구자의 출판 생산성과 명성(prestige)은
소속 기관의 위계적 위치에 강하게 영향받았다. 상위권 대학에서 하위권 대학으로 이동한 연구자는
생산성이 감소했고, 반대 방향의 이동은 생산성 증가와 연관되었다.{fn(39)}</p>

<h2 class="section-title" id="ch4-3">4.3 &nbsp; 다양성과 과학적 혁신</h2>
<p>연구팀의 다양성은 과학적 혁신에 어떤 영향을 미치는가? 성별 다양성의 효과를 분석한 대규모 연구에 따르면,
성별 다양성이 높은 팀이 더 참신하고 영향력 높은 과학적 아이디어를 생산했다.
640만 편의 논문과 230만 건의 특허를 분석한 결과, 혼성 팀의 논문은 동성 팀보다
인용에서 상위 5%에 들 확률이 유의하게 높았다.{fn(40)}</p>

<p>그러나 다양성의 효과는 단순하지 않다. "다양성-혁신 역설"이라 불리는 현상이 발견되었다.
소수 집단 출신 연구자들이 더 참신한 기여를 하는 경향이 있음에도 불구하고,
학계에서의 수용과 인정에서는 체계적으로 할인되었다.
즉, 다양성은 혁신의 원천이지만, 그 혁신이 제대로 인정받지 못하는 구조적 모순이 존재한다.{fn(41)}</p>

<p>인종적·민족적 다양성의 효과도 주목할 만하다.
900만 편 이상의 논문을 분석한 결과, 팀의 민족적 다양성이 과학적 영향력과 가장 강한 양의 상관관계를 보였다.
민족적 다양성은 성별 다양성이나 기관 다양성보다 더 강한 예측 변수였으며,
이는 다양한 문화적 배경이 문제에 대한 다양한 접근법을 가져오기 때문으로 해석되었다.{fn(42)}</p>

<p>성별과 민족 각각의 효과를 넘어, 이 두 축이 교차하는 지점에서 불평등은 더 심화된다.
유색인종 여성 과학자들은 성별과 인종의 이중 불이익을 경험한다.
US 기반 연구자 데이터를 분석한 결과, 흑인 여성 과학자의 연구비 수주율은 백인 남성의 약 절반에 불과했으며,
이러한 격차는 경력 단계가 올라갈수록 확대되었다.{fn(43)}</p>

<p>성별 불평등의 역사적 궤적을 50년 이상의 데이터로 추적한 연구는 일부 진전과 함께
지속적인 격차를 보여준다. 1950년대 이후 여성 연구자의 비율은 꾸준히 증가했지만,
2020년 현재에도 대부분의 STEM 분야에서 여성의 비율은 40% 미만이며,
특히 교신저자와 단독저자 비율에서 격차가 두드러졌다.{fn(44)}</p>

<h2 class="section-title" id="ch4-4">4.4 &nbsp; 멘토십과 샤페론 효과</h2>
<p>과학적 성공에서 멘토십의 역할은 무엇인가? "샤페론 효과(chaperone effect)"는
고영향력 저널에서의 첫 출판이 해당 저널에 이미 논문을 낸 시니어 연구자의 공저를 통해
이루어지는 현상을 지칭한다. Nature, Science, PNAS 등 주요 저널을 분석한 결과,
시니어 저자가 "게이트키퍼" 역할을 하며, 이러한 샤페론 없이 고영향력 저널에 처음 논문을 낼 확률은
매우 낮았다. 이 효과는 의학·생물학에서 가장 강하고 자연과학에서 상대적으로 약했다.{fn(45)}</p>

<p>성별에 따른 멘토십의 다양성 효과도 주목할 만하다.
과학적 다양성이 풍부한 환경에서 경력을 시작한 연구자는 이후에도 다양한 배경의 공저자와 협업하는 경향이
유의하게 높았다. 반면, 초기 경력에서 동질적 환경에 노출된 연구자는 이후에도 유사한 패턴을 반복했다.
다양성에 대한 노출은 "성장기"에 결정적 영향을 미치며, 이를 통한 긍정적 효과가 경력 전반에 지속되었다.{fn(46)}</p>

<p>과학 인력의 글로벌 이동도 과학 생태계의 핵심 동역학이다.
전 세계 연구자의 이동 패턴을 분석한 결과, 과학적 이주는 경제 발전 수준과 강한 상관관계를 보였다.
고소득 국가로의 두뇌 유출이 지속되는 한편, 중국·인도 등에서의 역이주(return migration)도
최근 증가 추세에 있어 글로벌 과학 인력 분포가 재편되고 있다.{fn(47)}</p>

{table_html(
    ['요인', '주요 발견', '영향 방향', '근거'],
    [
        ['팀 규모', '소규모 팀이 파괴적 혁신, 대규모 팀이 점진적 개선', '↔ 역설적', 'Wu et al. (2019)'],
        ['성별 다양성', '혼성 팀이 더 참신한 아이디어 생산', '↑ 긍정적', 'Yang et al. (2022)'],
        ['민족 다양성', '가장 강한 영향력 예측 변수', '↑ 긍정적', 'AlShebli et al. (2018)'],
        ['물리적 근접성', '원격 협업은 파괴적 혁신 저하', '↑ 근접 유리', 'Lin et al. (2023)'],
        ['초기 좌절', '근소 실패 그룹이 장기적으로 더 높은 성과', '↑ 역설적 긍정', 'Wang et al. (2019)'],
        ['기관 위계', '상위 기관 소속이 생산성과 명성에 유리', '↑ 위계 의존', 'Way et al. (2019)'],
        ['샤페론 효과', '시니어 공저자가 고영향력 저널 진입 게이트키퍼', '↑ 네트워크 의존', 'Sekara et al. (2018)'],
    ]
)}

{challenge_box('과학 인력과 협업의 핵심 도전', [
    '다양성 역설: 소수 집단이 더 참신한 기여를 하지만 그 기여가 체계적으로 할인되는 구조적 모순.',
    '원격 협업의 한계: 팬데믹 이후 원격 협업이 증가했으나, 파괴적 혁신에는 물리적 근접성이 여전히 중요.',
    '멘토십의 불평등: 샤페론 효과는 기존 네트워크를 가진 연구자에게 유리하며, 네트워크 밖의 재능이 발견되지 못할 위험.',
    '두뇌 유출: 고소득 국가로의 인력 편중이 글로벌 과학 역량의 불균형을 심화.',
])}

<div class="figure">
{img_tag('fig_ch4.png', '제4장 핵심 그림', 'chapter-fig')}
</div>

{arrow('제4장 요약: 팀 규모·다양성·멘토십·이동성이 과학적 혁신과 경력을 복잡하게 형성한다. → AI와 LLM의 등장은 이 모든 동역학을 어떻게 변화시킬 것인가?')}

</div>
</section>
"""



def build_ch5():
    return f"""
<section class="chapter" id="ch5">
{cover_banner('cover_ch5.png', '제5장')}
<div class="chapter-body">
<h1 class="chapter-title" id="ch5-top">제5장 &nbsp; AI와 LLM이 바꾸는 SciSci</h1>

<h2 class="section-title" id="ch5-1">5.1 &nbsp; AI가 여는 과학적 발견의 새 시대</h2>
<p>인공지능이 과학적 발견의 패러다임을 바꾸고 있다.
이 변화의 폭과 깊이를 조망한 종합 리뷰에 따르면, AI는 가설 생성, 실험 설계, 데이터 분석,
결과 해석이라는 과학적 방법의 모든 단계에 침투하고 있다.
자기 지도 학습이 단백질 구조 예측에서 실험 수준의 정확도를 달성하고,
기하학적 딥러닝이 분자 속성 예측 오차를 획기적으로 줄이며,
생성형 AI가 신약 후보 발굴 시간을 수년에서 수주로 단축한 사례들이 보고되고 있다.{fn(48)}</p>

<p>이 변화의 가장 상징적 사례가 AlphaFold이다.
DeepMind가 개발한 이 딥러닝 모델은 아미노산 서열만으로 단백질의 3차원 구조를 예측하며,
CASP14 대회에서 GDT 점수 92.4를 기록하여 실험적 방법(X선 결정학, 크라이오전자현미경)과
대등한 정확도를 달성했다. 2억 개 이상의 단백질 구조 예측이 공개되어
구조생물학의 연구 방식 자체를 변혁했다.{fn(49)}</p>

<p>재료과학에서도 AI의 발견 능력이 입증되었다.
Google DeepMind의 GNoME(Graph Networks for Materials Exploration)는
그래프 신경망을 활용하여 220만 개의 새로운 결정 구조를 예측했으며,
이 중 380,000개가 열역학적으로 안정한 것으로 확인되었다.
이는 인류가 역사상 발견한 안정 결정 수의 약 10배에 해당하는 규모로,
AI가 재료 탐색 공간을 극적으로 확장할 수 있음을 보여주었다.{fn(50)}</p>

<p>자연어 처리를 통한 잠재적 지식 발굴도 주목할 만하다.
재료과학 논문 330만 편의 초록에 Word2Vec을 적용한 결과, 모델이 명시적으로 학습하지 않은
재료의 열전 특성을 예측할 수 있었다. 알고리즘이 추천한 상위 50개 후보 중 다수가
이후 실험으로 확인되었으며, 일부는 연구자들이 아직 탐색하지 않은 새로운 후보였다.
문헌에 묻혀 있는 암묵적 지식을 AI가 발굴할 수 있음을 시사하는 결과이다.{fn(51)}</p>

<h2 class="section-title" id="ch5-2">5.2 &nbsp; LLM과 과학 생산성</h2>
<p>대규모 언어 모델(LLM)의 등장은 과학 글쓰기와 커뮤니케이션에 즉각적 변화를 가져왔다.
ChatGPT 출시 이후 학술 논문에서 특정 영어 단어—"delve", "intricate", "commendable" 등—의 빈도가
급격히 증가했다는 분석은 LLM이 이미 과학 글쓰기에 광범위하게 사용되고 있음을 시사한다.
논문 수준에서 LLM 사용 추정치는 분야에 따라 7-17%에 달했다.{fn(52)}</p>

<p>글쓰기 스타일의 변화가 표면적 현상이라면, 더 근본적인 문제는 AI가 과학의 방향 자체를 바꾸고 있다는 점이다.
2026년 Nature에 발표된 대규모 분석에 따르면, AI 도구를 사용하는 과학자의 개인 생산성은
유의하게 증가했지만, 동시에 과학 연구의 주제 다양성은 감소했다.
AI가 이미 잘 작동하는 영역에 연구를 집중시키는 "편향 증폭" 효과가 관찰된 것이다.
개인 수준의 효율성 향상이 집합적 수준의 탐색 범위 축소로 이어질 수 있다는 경고이다.{fn(53)}</p>

<h2 class="section-title" id="ch5-3">5.3 &nbsp; SciSciGPT: AI 기반 과학 측정학</h2>
<p>AI는 과학을 연구하는 것뿐 아니라, 과학의 과학(SciSci) 자체의 도구로도 활용되고 있다.
SciSciGPT는 GPT-4를 기반으로 과학 측정학 분석을 자동화하는 AI 에이전트이다.
사용자가 자연어로 "최근 10년간 AI 분야의 협업 패턴 변화를 분석해줘"와 같은 질문을 하면,
적절한 데이터셋을 선택하고, 분석 코드를 생성·실행하며, 결과를 시각화하고 해석까지 수행한다.
전문가 수준의 SciSci 분석 파이프라인을 비전문가도 접근할 수 있게 만드는 것이 목표이다.{fn(54)}</p>

<p>LLM이 SciSci에 가져올 변화에 대한 포괄적 전망도 제시되었다.
연구 동향 분석, 연구자 경력 궤적 예측, 학제 간 연결 발견, 연구비 배분 최적화,
과학 정책 시뮬레이션 등 SciSci의 거의 모든 하위 분야에서 LLM이 기존 방법론을 보완하거나
대체할 잠재력이 있다. 다만, LLM의 "환각(hallucination)" 문제와 훈련 데이터 편향이
SciSci 분석의 신뢰성에 미칠 위험도 함께 지적되었다.{fn(55)}</p>

<h2 class="section-title" id="ch5-4">5.4 &nbsp; 자율적 과학 에이전트</h2>
<p>과학 문헌을 읽고 종합하는 수준을 넘어, 연구의 전 과정을 자동화하려는 시도가 본격화되고 있다.
"AI Scientist"는 아이디어 생성부터 실험 설계·실행, 결과 분석, 논문 작성,
심지어 동료 심사까지 수행하는 완전 자동화 시스템이다.
GPT-4를 기반으로 머신러닝 연구 분야에서 논문 한 편을 생성하는 데 약 15달러의 비용이 소요되며,
생성된 논문은 인간 심사자로부터 주요 ML 학회의 약한 수락(weak accept) 수준의 평가를 받았다.{fn(56)}</p>

<p>자동화의 기회와 위험이 교차하는 현실에서, 실제 실험 자동화의 성공 사례도 등장했다.
Coscientist는 GPT-4를 엔진으로 하는 자율적 화학 연구 에이전트로,
인터넷 검색, 문헌 조사, 실험 프로토콜 설계, 로봇 실험실 제어를 자율적으로 수행한다.
팔라듐 촉매 교차 커플링 반응을 성공적으로 최적화한 사례가 보고되었으며,
이는 LLM이 디지털 세계뿐 아니라 물리적 실험실까지 제어할 수 있음을 보여주었다.{fn(57)}</p>

<p>재료과학에서도 비슷한 발견이 이어졌다.
ChemCrow는 18개의 전문 도구를 통합한 LLM 기반 화학 에이전트로,
유기 합성 계획, 약물 발견, 재료 설계 등의 작업을 수행한다.
전문가 평가에서 ChemCrow의 솔루션은 기본 GPT-4보다 유의하게 높은 정확도를 보였으며,
특히 다단계 합성 경로 계획에서 강점을 나타냈다.{fn(58)}</p>

<p>이러한 변화가 과학이라는 활동 자체에 어떤 함의를 갖는지에 대한 성찰도 이어지고 있다.
과학 실천의 자동화가 가져올 기회와 도전을 분석한 포괄적 리뷰는,
AI가 과학의 민주화(비전문가의 연구 참여 확대)와 동시에 과학의 획일화(AI가 선호하는 방향으로의 수렴)를
가져올 수 있다고 경고한다. 특히, AI가 생성한 가설이 검증 없이 순환적으로 인용되는
"자기참조적 지식 루프"의 위험이 강조되었다.{fn(59)}</p>

<p>LLM이 과학 문헌을 종합하는 능력도 이미 인간 수준에 도달하고 있다.
PaperQA2 시스템은 과학 논문에 대한 질의응답과 문헌 종합에서 인간 전문가와 비교하여
정확도에서 대등하거나 우수한 성능을 보였다. 특히 200편 이상의 논문을 동시에 종합하는 과제에서
AI는 인간이 물리적으로 수행하기 어려운 규모의 문헌 리뷰를 가능하게 했다.{fn(60)}</p>

{table_html(
    ['AI 시스템', '연도', '능력', '성과', '한계'],
    [
        ['AlphaFold', '2021', '단백질 구조 예측', 'GDT 92.4, 2억+ 구조 예측', '동적 구조, 복합체 한계'],
        ['GNoME', '2023', '결정 구조 발견', '220만 신규 구조, 38만 안정', '합성 가능성 미검증'],
        ['Coscientist', '2023', '자율 화학 실험', '팔라듐 촉매 반응 최적화', '제한된 실험 범위'],
        ['ChemCrow', '2024', '화학 도구 통합', '다단계 합성 경로 계획', '도구 의존적, 검증 필요'],
        ['AI Scientist', '2024', '완전 자동 연구', '논문 1편 ~$15, 약한 수락 수준', '창의성·독창성 의문'],
        ['SciSciGPT', '2025', 'SciSci 분석 자동화', '자연어→분석→시각화', '환각 위험, 데이터 의존'],
        ['PaperQA2', '2024', '초인적 문헌 종합', '인간 전문가 대등/우수', '최신 논문 반영 지연'],
    ]
)}

{challenge_box('AI 기반 과학의 핵심 위험', [
    '환각과 신뢰성: LLM이 생성한 과학적 주장이 사실처럼 보이지만 실제로는 허구인 경우, 이를 걸러낼 메커니즘이 부재.',
    '자기참조적 루프: AI가 생성한 가설이 검증 없이 인용되고, 다시 AI 훈련 데이터에 포함되는 순환 오류의 위험.',
    '탐색 범위 축소: AI가 잘 작동하는 영역에 연구가 집중되어 과학의 다양성과 세렌디피티가 감소할 가능성.',
    '책임과 저자성: AI가 논문을 작성하고 실험을 수행할 때, 과학적 발견의 책임과 공로는 누구에게 귀속되는가?',
    '접근성 격차: AI 도구에 대한 접근이 불균등하여 "AI 부국"과 "AI 빈국" 간 과학 격차가 확대될 수 있음.',
])}

<div class="figure">
{img_tag('fig_ch5.png', '제5장 핵심 그림', 'chapter-fig')}
</div>

{arrow('제5장 요약: AI와 LLM은 과학적 발견을 가속화하는 동시에 과학의 다양성·신뢰성·공정성에 새로운 도전을 제기한다. → 이러한 변화 속에서 과학 정책과 제도는 어떻게 대응하고 있는가?')}

</div>
</section>
"""


def build_ch6():
    return f"""
<section class="chapter" id="ch6">
{cover_banner('cover_ch6.png', '제6장')}
<div class="chapter-body">
<h1 class="chapter-title" id="ch6-top">제6장 &nbsp; 과학 정책, 재현성, 미래</h1>

<h2 class="section-title" id="ch6-1">6.1 &nbsp; 재현성 위기의 실체</h2>
<p>과학의 신뢰성은 재현 가능성에 기초한다. 그러나 2005년, 의학 연구의 상당수가 재현 불가능하다는 이론적 경고가 제기되었다.
출판 편향, 소규모 표본, p-해킹(p-hacking), 이해충돌이 결합하면
"출판된 연구 결과의 대부분이 거짓일 수 있다"는 도발적 주장이었다.
시뮬레이션을 통해, 일반적인 연구 조건에서 양성 예측값(PPV)이 50% 미만으로 떨어질 수 있음이 보여졌다.{fn(61)}</p>

<p>이론적 경고가 현실에서도 확인된 것은 대규모 설문과 직접 재현 연구를 통해서였다.
1,576명의 연구자를 대상으로 한 Nature 설문 결과, 우려는 현실이었다.
응답자의 70% 이상이 다른 연구자의 실험을 재현하는 데 실패한 경험이 있었고,
52%는 "심각한 재현성 위기"가 존재한다고 답했다.
화학, 생물학, 물리학, 의학 순으로 재현 실패율이 높았다.{fn(62)}</p>

<p>설문이 인식을 측정한 것이라면, 실제로 재현을 시도한 결과는 어떠한가?
Open Science Collaboration은 심리학의 상위 저널에 발표된 100편의 연구를 체계적으로 재현 시도했다.
결과는 충격적이었다. 원래 97%의 연구가 통계적으로 유의한 결과를 보고했지만,
재현 시도에서는 단 36%만이 유의한 결과를 얻었다. 평균 효과 크기도 원본의 절반 수준이었다.{fn(63)}</p>

<p>사회과학 실험의 재현성도 체계적으로 검증되었다.
Nature와 Science에 게재된 21개의 사회과학 실험을 재현한 결과,
62%에서 원래의 효과가 같은 방향으로 재현되었지만, 효과 크기는 평균적으로 원본의 약 50%에 불과했다.
이론적 경고, 현장의 체감, 직접 검증 — 세 가지 경로가 수렴적으로
과학의 재현성에 심각한 문제가 있음을 확인한 것이다.{fn(64)}</p>

<h2 class="section-title" id="ch6-2">6.2 &nbsp; 과학적 부정행위와 편향</h2>
<p>재현성 위기의 한 축에는 의도적 부정행위가 있다.
PubMed에서 철회된 2,047편의 논문을 분석한 결과, 철회 사유의 67.4%가 부정행위(사기, 데이터 조작, 표절)였으며,
단순 오류에 의한 철회는 21.3%에 불과했다. 이는 과학 문헌의 오류 대부분이
"선의의 실수"가 아니라 "의도적 왜곡"에서 비롯된다는 불편한 현실을 드러낸다.{fn(65)}</p>

<p>부정행위까지 가지 않더라도, 과학적 편향은 더 광범위한 문제이다.
1,910편의 메타분석을 포괄하는 메타-메타분석에서,
과학 연구에서 편향의 크기와 방향을 체계적으로 평가한 결과,
소규모 연구일수록 효과 크기가 과대 추정되는 경향이 뚜렷했다.
이 "소규모 연구 효과(small-study effect)"는 출판 편향의 간접적 증거로,
유의하지 않은 결과가 출판되지 않는 "파일 서랍 문제"의 규모를 시사한다.{fn(66)}</p>

<h2 class="section-title" id="ch6-3">6.3 &nbsp; 연구비 배분의 과학</h2>
<p>과학 정책의 핵심 질문 중 하나는 한정된 연구비를 어떻게 배분할 것인가이다.
동료 심사(peer review) 기반의 연구비 배분이 최선의 연구를 선별하는지에 대한 의문이 제기되었다.
NIH의 연구비 심사를 분석한 결과, 심사위원의 점수와 이후 연구 성과(인용, 특허) 사이에
유의미한 상관관계를 찾기 어려웠다. "빅네임"이 "빅아이디어"보다 유리한 현상이 발견된 것이다.{fn(67)}</p>

<p>연구비 배분에서의 "마태 효과(Matthew effect)"도 실증적으로 확인되었다.
이미 연구비를 많이 받은 연구자가 추가 연구비를 받을 확률이 불균형적으로 높았으며,
이는 연구의 질보다 기존의 명성과 네트워크에 의해 결정되는 부분이 컸다.
이 편향은 특히 초기 경력 연구자와 비주류 기관의 연구자에게 불리하게 작용했다.{fn(68)}</p>

<p>이러한 문제에 대한 급진적 대안으로 "연구비 추첨제"가 제안되고 실험되고 있다.
최소 품질 기준을 통과한 제안서 중에서 무작위로 수혜자를 선정하는 방식이다.
뉴질랜드 건강연구위원회, 스위스 국립과학재단, 오스트리아 과학재단 등이
부분적 추첨제를 도입했으며, 이는 심사의 주관성과 편향을 줄이면서도
연구의 다양성을 높이는 효과가 있는 것으로 초기 평가되고 있다.{fn(69)}</p>

<p>과학의 진보가 세대 교체와 어떤 관계를 갖는지에 대한 연구도 흥미롭다.
"과학은 장례식이 있어야 진보하는가?"라는 도발적 질문에 답하기 위해,
저명한 과학자의 예기치 않은 사망이 해당 분야에 미치는 영향을 분석한 결과,
스타 과학자의 사망 후 해당 분야에 새로운 연구자의 진입이 증가했고,
이들은 기존과 다른 접근법으로 유의한 기여를 했다.
기존 권위자가 새로운 아이디어의 진입 장벽으로 작용할 수 있음을 시사하는 결과이다.{fn(70)}</p>

<p>유사한 맥락에서, 저명 과학자의 갑작스러운 은퇴가 해당 분야의 후속 연구에 미치는 영향도 연구되었다.
"슈퍼스타 소멸" 효과는 해당 연구자의 직접적 공저자뿐 아니라,
같은 분야의 비공저자에게도 영향을 미쳤으며, 이는 지적 리더십의 상실이
분야 전체의 연구 방향과 자원 배분에 파급 효과를 가짐을 보여준다.{fn(71)}</p>

<h2 class="section-title" id="ch6-4">6.4 &nbsp; 팬데믹과 과학-정책 공진화</h2>
<p>COVID-19 팬데믹은 과학과 정책의 관계를 전례 없는 속도로 재편했다.
통상 과학적 발견이 정책에 반영되기까지는 수년이 소요된다.
논문 출판, 동료 심사, 합의 형성이라는 느린 파이프라인이 필요하기 때문이다.
그러나 팬데믹 기간 동안 과학 논문이 정책 문서에 인용되기까지의 지연 시간이
극적으로 단축되었다. 114개국의 37,725건 정책 문서를 분석한 결과,
인용 지연 중앙값이 기존 대비 수개월에서 수일 수준으로 감소했다.{fn(72)}</p>

<p>과학의 공공 활용과 공공 자금 지원 사이의 관계도 조명되었다.
대규모 데이터 분석에 따르면, 공적 자금으로 지원된 연구는 민간 자금 연구보다
정부 문서, 위키피디아, 뉴스 미디어에서 더 많이 인용되는 경향이 있었다.
특히 기초연구의 공공 활용도가 응용연구보다 높았으며, 이는 기초연구에 대한
공공 투자의 사회적 회수가 장기적이지만 광범위함을 시사한다.{fn(73)}</p>

<p>과학적 보상 체계의 구조도 분석되었다.
STEM 분야의 주요 학술상 수상 네트워크를 분석한 결과, 상의 배분이
고도로 집중된 "부익부" 패턴을 따랐다. 소수의 연구자가 여러 개의 상을 수상하는 반면,
대다수는 한 번도 수상하지 못하는 극단적 불균등이 관찰되었다.
이는 과학적 인정 체계가 다양한 기여를 포착하기보다는 기존의 불평등을 강화하는 방향으로 작동할 수 있음을 보여준다.{fn(74)}</p>

{table_html(
    ['정책 과제', '현재 상태', '제안된 대안', '근거'],
    [
        ['재현성', '심리학 36%, 사회과학 62% 재현', '사전 등록, 오픈 데이터 의무화', 'OSC (2015)'],
        ['연구비 배분', '명성 편향, 낮은 예측 타당도', '추첨제, 블라인드 심사', 'Li & Agha (2015)'],
        ['과학적 부정행위', '철회 논문의 67%가 부정행위', '데이터 공유 의무화, AI 탐지', 'Fang et al. (2012)'],
        ['과학-정책 연계', '팬데믹 시 인용 지연 극적 감소', '실시간 과학 자문 체계 구축', 'Yin et al. (2021)'],
        ['보상 불평등', '소수에게 상이 집중', '기여 기반 다원적 인정 체계', 'Ma et al. (2018)'],
        ['AI 통합', '과학 자동화 가속', '윤리 가이드라인, 투명성 요구', 'Gil et al. (2025)'],
    ]
)}

{challenge_box('과학 정책과 제도의 핵심 과제', [
    '"출판 아니면 소멸(publish or perish)" 문화가 속도를 우선시하고 재현성을 소홀히 하는 원인.',
    '데이터·코드 공유 의무화가 확산되고 있으나, 인센티브 부족과 인프라 미비로 실천율은 여전히 낮음.',
    'AI 공저자 인정, AI 생성 데이터의 신뢰성 검증, 알고리즘적 편향의 과학적 영향에 대한 규범 부재.',
    '국가 간 연구 역량 격차가 확대되는 가운데, 글로벌 도전(기후변화, 팬데믹)에 대한 조율된 과학적 대응이 필요.',
])}

<div class="figure">
{img_tag('fig_ch6.png', '제6장 핵심 그림', 'chapter-fig')}
</div>

{arrow('제6장 요약: 재현성 위기, 연구비 배분의 편향, AI의 급속한 통합이라는 세 가지 도전 속에서, 과학 정책은 인센티브 구조의 근본적 재설계를 요구받고 있다.')}

</div>
</section>
"""


def build_references():
    REFERENCES = [
        ('Price, D. J. de S.', 'Networks of Scientific Papers', 'Science', '149(3683), 510-515', 1965, '10.1126/science.149.3683.510'),
        ('Garfield, E.', 'Citation Analysis as a Tool in Journal Evaluation', 'Science', '178(4060), 471-479', 1972, '10.1126/science.178.4060.471'),
        ('Price, D. J. de S.', 'A General Theory of Bibliometric and Other Cumulative Advantage Processes', 'JASIS', '27(5), 292-306', 1976, '10.1002/asi.4630270505'),
        ('Watts, D. J. & Strogatz, S. H.', 'Collective Dynamics of Small-World Networks', 'Nature', '393, 440-442', 1998, '10.1038/30918'),
        ('Barabasi, A.-L. & Albert, R.', 'Emergence of Scaling in Random Networks', 'Science', '286(5439), 509-512', 1999, '10.1126/science.286.5439.509'),
        ('Newman, M. E. J.', 'The Structure of Scientific Collaboration Networks', 'PNAS', '98(2), 404-409', 2001, '10.1073/pnas.98.2.404'),
        ('Barabasi, A.-L. et al.', 'Evolution of the Social Network of Scientific Collaborations', 'Physica A', '311(3-4), 590-614', 2002, '10.1016/S0378-4371(02)00736-7'),
        ('Blondel, V. D. et al.', 'Fast Unfolding of Communities in Large Networks', 'JSTAT', '2008(10), P10008', 2008, '10.1088/1742-5468/2008/10/P10008'),
        ('Fortunato, S.', 'Community Detection in Graphs', 'Physics Reports', '486(3-5), 75-174', 2010, '10.1016/j.physrep.2009.11.002'),
        ('Van Eck, N. J. & Waltman, L.', 'Software Survey: VOSviewer', 'Scientometrics', '84(2), 523-538', 2010, '10.1007/s11192-009-0146-3'),
        ('Boyack, K. W. & Klavans, R.', 'Co-Citation Analysis, Bibliographic Coupling, and Direct Citation', 'JASIST', '61(12), 2389-2404', 2010, '10.1002/asi.21419'),
        ('Azoulay, P. et al.', 'Superstar Extinction', 'Quarterly Journal of Economics', '125(2), 549-589', 2010, '10.1162/qjec.2010.125.2.549'),
        ('Borner, K. et al.', 'Design and Update of a Classification System: The UCSD Map of Science', 'PLOS ONE', '7(7), e39464', 2012, '10.1371/journal.pone.0039464'),
        ('Fang, F. C. et al.', 'Misconduct Accounts for the Majority of Retracted Scientific Publications', 'PNAS', '109(42), 17028-17033', 2012, '10.1073/pnas.1212247109'),
        ('Wang, D., Song, C. & Barabasi, A.-L.', 'Quantifying Long-term Scientific Impact', 'Science', '342(6154), 127-132', 2013, '10.1126/science.1237825'),
        ('Uzzi, B. et al.', 'Atypical Combinations and Scientific Impact', 'Science', '342(6154), 468-472', 2013, '10.1126/science.1240474'),
        ('Lariviere, V. et al.', 'Bibliometrics: Global Gender Disparities in Science', 'Nature', '504, 211-213', 2013, '10.1038/504211a'),
        ('Shen, H. & Barabasi, A.-L.', 'Collective Credit Allocation in Science', 'PNAS', '111(34), 12325-12330', 2014, '10.1073/pnas.1401992111'),
        ('Milojevic, S.', 'Principles of Scientific Research Team Formation and Evolution', 'PNAS', '111(11), 3984-3989', 2014, '10.1073/pnas.1309723111'),
        ('Ke, Q. et al.', 'Defining and Identifying Sleeping Beauties in Science', 'PNAS', '112(24), 7426-7431', 2015, '10.1073/pnas.1424329112'),
        ('Li, D. & Agha, L.', 'Big Names or Big Ideas', 'Science', '348(6233), 434-438', 2015, '10.1126/science.aaa0185'),
        ('Open Science Collaboration', 'Estimating the Reproducibility of Psychological Science', 'Science', '349(6251), aac4716', 2015, '10.1126/science.aac4716'),
        ('Lariviere, V. et al.', 'The Oligopoly of Academic Publishers in the Digital Era', 'PLOS ONE', '10(6), e0127502', 2015, '10.1371/journal.pone.0127502'),
        ('Bornmann, L. & Mutz, R.', 'Growth Rates of Modern Science', 'JASIST', '66(11), 2215-2222', 2015, '10.1002/asi.23329'),
        ('Egghe, L.', 'Theory and Practice of the g-index', 'Scientometrics', '69(1), 131-152', 2006, '10.1007/s11192-006-0144-7'),
        ('Hirsch, J. E.', "An Index to Quantify an Individual's Scientific Research Output", 'PNAS', '102(46), 16569-16572', 2005, '10.1073/pnas.0507655102'),
        ('Hutchins, B. I. et al.', 'Relative Citation Ratio (RCR)', 'PLOS Biology', '14(9), e1002541', 2016, '10.1371/journal.pbio.1002541'),
        ('Baker, M.', '1,500 Scientists Lift the Lid on Reproducibility', 'Nature', '533, 452-454', 2016, '10.1038/533452a'),
        ('Funk, R. J. & Owen-Smith, J.', 'A Dynamic Network Measure of Technological Change', 'Management Science', '63(3), 791-817', 2017, '10.1287/mnsc.2015.2366'),
        ('Fanelli, D. et al.', 'Meta-assessment of Bias in Science', 'PNAS', '114(14), 3714-3719', 2017, '10.1073/pnas.1618569114'),
        ('Way, S. F. et al.', 'The Misleading Narrative of the Canonical Faculty Productivity Trajectory', 'PNAS', '114(44), E9216-E9223', 2017, '10.1073/pnas.1702121114'),
        ('Fortunato, S. et al.', 'Science of Science', 'Science', '359(6379), eaao0185', 2018, '10.1126/science.aao0185'),
        ('Liu, L. et al.', 'Hot Streaks in Artistic, Cultural, and Scientific Careers', 'Nature', '559, 396-399', 2018, '10.1038/s41586-018-0315-8'),
        ('Gerlach, M. et al.', 'A Network Approach to Topic Models', 'Science Advances', '4(7), eaaq1360', 2018, '10.1126/sciadv.aaq1360'),
        ('Bol, T. et al.', 'The Matthew Effect in Science Funding', 'PNAS', '115(19), 4887-4890', 2018, '10.1073/pnas.1719557115'),
        ('Camerer, C. F. et al.', 'Evaluating the Replicability of Social Science Experiments', 'Nature Human Behaviour', '2, 637-644', 2018, '10.1038/s41562-018-0399-z'),
        ('Sekara, V. et al.', 'The Chaperone Effect in Scientific Publishing', 'PNAS', '115(50), 12603-12607', 2018, '10.1073/pnas.1800471115'),
        ('AlShebli, B. K. et al.', 'The Preeminence of Ethnic Diversity in Scientific Collaboration', 'Nature Communications', '9, 5163', 2018, '10.1038/s41467-018-07634-8'),
        ('Ma, Y. et al.', 'Principled Discovery of Science Prize Network', 'PNAS', '115(48), 12135-12140', 2018, '10.1073/pnas.1800485115'),
        ('Piwowar, H. et al.', 'The State of OA: A Large-Scale Analysis', 'PeerJ', '6, e4375', 2018, '10.7717/peerj.4375'),
        ('Wu, L., Wang, D. & Evans, J. A.', 'Large Teams Develop and Small Teams Disrupt Science and Technology', 'Nature', '566, 378-382', 2019, '10.1038/s41586-019-0941-9'),
        ('Wang, Y. et al.', 'Early-Career Setback and Future Career Impact', 'Nature Communications', '10, 4331', 2019, '10.1038/s41467-019-12189-3'),
        ('Yin, Y. et al.', 'Quantifying the Dynamics of Failure Across Science, Startups, and Security', 'Nature', '575, 190-194', 2019, '10.1038/s41586-019-1725-y'),
        ('Way, S. F. et al.', 'Productivity, Prominence, and the Effects of Academic Environment', 'PNAS', '116(22), 10729-10733', 2019, '10.1073/pnas.1817431116'),
        ('Tshitoyan, V. et al.', 'Unsupervised Word Embeddings Capture Latent Knowledge from Materials Science Literature', 'Nature', '571, 95-98', 2019, '10.1038/s41586-019-1335-8'),
        ('Azoulay, P. et al.', 'Does Science Advance One Funeral at a Time?', 'American Economic Review', '109(8), 2889-2920', 2019, '10.1257/aer.20161574'),
        ('Freeman, R. B. & Huang, W.', 'Making Gender Diversity Work for Scientific Discovery and Innovation', 'Nature Human Behaviour', '3, 1040-1041', 2019, '10.1038/s41562-018-0433-1'),
        ('Radicchi, F. et al.', 'Universality of Citation Distributions', 'PNAS', '105(45), 17268-17272', 2008, '10.1073/pnas.0806977105'),
        ('Hofstra, B. et al.', 'The Diversity-Innovation Paradox in Science', 'PNAS', '117(17), 9284-9291', 2020, '10.1073/pnas.1915378117'),
        ('Ioannidis, J. P. A. et al.', 'Updated Science-Wide Author Databases of Standardized Citation Indicators', 'PLOS Biology', '18(10), e3000918', 2020, '10.1371/journal.pbio.3000918'),
        ('Huang, J. et al.', 'Historical Comparison of Gender Inequality in Scientific Careers', 'PNAS', '117(9), 4609-4616', 2020, '10.1073/pnas.1914221117'),
        ('Lo, K. et al.', 'S2ORC: The Semantic Scholar Open Research Corpus', 'ACL 2020', '', 2020, '10.18653/v1/2020.acl-main.447'),
        ('Yin, Y. et al.', 'Coevolution of Policy and Science During the Pandemic', 'Science', '371(6525), 128-131', 2021, '10.1126/science.abe3084'),
        ('Jumper, J. et al.', 'Highly Accurate Protein Structure Prediction with AlphaFold', 'Nature', '596, 583-589', 2021, '10.1038/s41586-021-03819-2'),
        ('Nielsen, M. W. & Andersen, J. P.', 'Global Citation Inequality Is on the Rise', 'PNAS', '118(7), e2012208118', 2021, '10.1073/pnas.2012208118'),
        ('Priem, J. et al.', 'OpenAlex: A Fully-Open Index of Scholarly Works', 'arXiv', '2205.01833', 2022, '10.48550/arXiv.2205.01833'),
        ('Yang, Y. et al.', 'Gender-Diverse Teams Produce More Novel and Higher-Impact Scientific Ideas', 'PNAS', '119(36), e2200841119', 2022, '10.1073/pnas.2200841119'),
        ('Kozlowski, D. et al.', 'Intersectional Inequalities in Science', 'PNAS', '119(2), e2113067119', 2022, '10.1073/pnas.2113067119'),
        ('Yin, Y. et al.', 'Public Use and Public Funding of Science', 'Nature Human Behaviour', '6, 1397-1410', 2022, '10.1038/s41562-022-01397-5'),
        ('Park, M. et al.', 'Papers and Patents Are Becoming Less Disruptive Over Time', 'Nature', '613, 138-144', 2023, '10.1038/s41586-022-05543-x'),
        ('Wang, H. et al.', 'Scientific Discovery in the Age of Artificial Intelligence', 'Nature', '620, 47-60', 2023, '10.1038/s41586-023-06221-2'),
        ('Merchant, A. et al.', 'Scaling Deep Learning for Materials Discovery', 'Nature', '624, 80-85', 2023, '10.1038/s41586-023-06735-9'),
        ('Boiko, D. A. et al.', 'Autonomous Chemical Research with Large Language Models', 'Nature', '624, 570-578', 2023, '10.1038/s41586-023-06792-0'),
        ('Zhao, Z. et al.', 'Global Patterns of Migration of Scholars with Economic Development', 'PNAS', '120(4), e2217937120', 2023, '10.1073/pnas.2217937120'),
        ('Roumbanis, L.', 'Rethink Funding by Putting the Lottery First', 'Nature Human Behaviour', '7, 1018-1019', 2023, '10.1038/s41562-023-01649-y'),
        ('Lin, Y., Frey, C. B. & Wu, L.', 'Remote Collaboration Fuses Fewer Breakthrough Ideas', 'Nature', '623, 987-991', 2023, '10.1038/s41586-022-04966-w'),
        ('Skarlinski, M. et al.', 'Language Agents Achieve Superhuman Synthesis of Scientific Knowledge', 'Nature Machine Intelligence', '', 2024, '10.1038/s42256-024-00912-7'),
        ('Lu, C. et al.', 'The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery', 'arXiv', '2408.06292', 2024, '10.48550/arXiv.2408.06292'),
        ('Bran, A. M. et al.', 'Augmenting Large Language Models with Chemistry Tools', 'Nature Machine Intelligence', '6, 525-535', 2024, '10.1038/s42256-024-00832-8'),
        ('Ioannidis, J. P. A.', 'Why Most Published Research Findings Are False', 'PLOS Medicine', '2(8), e124', 2005, '10.1371/journal.pmed.0020124'),
        ('Liu, Z. et al.', 'SciSciGPT: Advancing Human-AI Collaboration in the Science of Science', 'Nature Computational Science', '', 2025, '10.1038/s43588-025-00790-0'),
        ('Xu, H. et al.', 'The Empowerment of Science of Science by Large Language Models', 'arXiv', '2501.16150', 2025, '10.48550/arXiv.2501.16150'),
        ('Gil, Y. et al.', 'Automating the Practice of Science', 'PNAS', '122(2), e2401238121', 2025, '10.1073/pnas.2401238121'),
        ('Liang, W. et al.', 'Scientific Production in the Era of Large Language Models', 'Science', '389(6732), adw3000', 2025, '10.1126/science.adw3000'),
        ('Sourati, J. et al.', "AI Tools Expand Scientists' Impact but Contract Science's Focus", 'Nature', '', 2026, '10.1038/s41586-026-08756-0'),
        ('Wuchty, S., Jones, B. F. & Uzzi, B.', 'The Increasing Dominance of Teams in Production of Knowledge', 'Science', '316(5827), 1036-1039', 2007, '10.1126/science.1136099'),
        ('Jones, B. F.', 'The Burden of Knowledge and the Death of the Renaissance Man', 'Review of Economic Studies', '76(1), 283-317', 2009, '10.1111/j.1467-937X.2009.00531.x'),
    ]
    REFERENCES.sort(key=lambda x: (x[4], x[0]))
    items = []
    for i, (authors, title, journal, vol, year, doi) in enumerate(REFERENCES, 1):
        ref_text = f'[{i}] {authors} ({year}). &ldquo;{title}.&rdquo; <em>{journal}</em>'
        if vol:
            ref_text += f', {vol}'
        ref_text += '.'
        doi_url = f'https://doi.org/{doi}' if doi.startswith('10.') else doi
        items.append(f'<div class="ref-item">{ref_text} <a href="{doi_url}" target="_blank">{doi_url}</a></div>')
    body = '\n'.join(items)
    return f'<section id="references"><h2>참고문헌</h2>{body}</section>'



# ── JS ───────────────────────────────────────────────────
JS = """
// Progress bar
window.addEventListener('scroll', () => {
  const total = document.body.scrollHeight - window.innerHeight;
  const pct = total > 0 ? (window.scrollY / total) * 100 : 0;
  document.getElementById('progress-bar').style.width = pct + '%';
});

// Active TOC highlight
const sections = document.querySelectorAll('section[id], h2[id], h1[id]');
const tocLinks = document.querySelectorAll('.toc-section');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      tocLinks.forEach(l => l.classList.remove('active'));
      const id = e.target.id;
      const active = document.querySelector(`.toc-section[href="#${id}"]`);
      if (active) active.classList.add('active');
    }
  });
}, { rootMargin: '-20% 0px -70% 0px' });
sections.forEach(s => observer.observe(s));

// Scroll animation
const chapters = document.querySelectorAll('.chapter');
const chapObs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('visible'); }
  });
}, { threshold: 0.05 });
chapters.forEach(c => chapObs.observe(c));

// Hamburger
const ham = document.getElementById('hamburger');
const sidebar = document.getElementById('sidebar');
ham.addEventListener('click', () => sidebar.classList.toggle('open'));
document.getElementById('main').addEventListener('click', () => sidebar.classList.remove('open'));

// Smooth scroll for TOC links
document.querySelectorAll('.toc-section').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    const target = document.querySelector(link.getAttribute('href'));
    if (target) target.scrollIntoView({ behavior: 'smooth' });
    sidebar.classList.remove('open');
  });
});
"""

# ── Main builder ─────────────────────────────────────────
# Section → representative paper figure caption
SECTION_FIGURES = {
    "ch1-1": ("sec_1_1.png", "Fortunato et al. (2018) Science of Science"),
    "ch1-2": ("sec_1_2.png", "Newman (2001) Structure of Scientific Collaboration Networks"),
    "ch1-3": ("sec_1_3.png", "Barabási & Albert (1999) Scale-Free Networks"),
    "ch1-4": ("sec_1_4.png", "Guimerà et al. (2005) Team Assembly Mechanisms"),
    "ch2-1": ("sec_2_1.png", "Hirsch (2005) h-index"),
    "ch2-2": ("sec_2_2.png", "Park et al. (2023) Declining Disruptiveness"),
    "ch2-3": ("sec_2_3.png", "Ke et al. (2015) Sleeping Beauties"),
    "ch2-4": ("sec_2_4.png", "Larivière et al. (2015) Oligopoly of Academic Publishers"),
    "ch3-1": ("sec_3_1.png", "Radicchi et al. (2008) Citation Distributions"),
    "ch3-2": ("sec_3_2.png", "Börner et al. (2012) UCSD Map of Science"),
    "ch3-3": ("sec_3_3.png", "Fortunato (2010) Community Detection"),
    "ch3-4": ("sec_3_4.png", "Piwowar et al. (2018) State of OA"),
    "ch4-1": ("sec_4_1.png", "Wu et al. (2019) Large Teams vs Small Teams"),
    "ch4-2": ("sec_4_2.png", "Way et al. (2017) Faculty Productivity"),
    "ch4-3": ("sec_4_3.png", "Hofstra et al. (2020) Diversity-Innovation Paradox"),
    "ch4-4": ("sec_4_4.png", "Sekara et al. (2018) Chaperone Effect"),
    "ch5-1": ("sec_5_1.png", "Lu et al. (2024) The AI Scientist"),
    "ch5-2": ("sec_5_2.png", "Liang et al. (2025) LLM & Science of Science"),
    "ch5-3": ("sec_5_3.png", "Shao et al. (2025) SciSciGPT"),
    "ch5-4": ("sec_5_4.png", "Boiko et al. (2023) Autonomous Chemical Research"),
    "ch6-1": ("sec_6_1.png", "Open Science Collaboration (2015) Reproducibility"),
    "ch6-2": ("sec_6_2.png", "Grieneisen & Zhang (2012) Retracted Articles Survey"),
    "ch6-3": ("sec_6_3.png", "Shah et al. (2018) Design and Analysis of Peer Review"),
    "ch6-4": ("sec_6_4.png", "Azoulay et al. (2019) Does Science Advance One Funeral at a Time?"),
}


def inject_section_figures(html):
    """Post-process HTML to inject section paper figures after each h2 section title."""
    import re
    for sec_id, (fig_file, caption) in SECTION_FIGURES.items():
        src = img_b64(fig_file)
        if src is None:
            continue
        pattern = f'(<h2 class="section-title" id="{sec_id}">.*?</h2>)'
        fig_html = (
            f'\\1\n'
            f'<figure class="section-figure">'
            f'<img src="{src}" alt="{caption}">'
            f'<figcaption>{caption}</figcaption>'
            f'</figure>'
        )
        html = re.sub(pattern, fig_html, html, count=1)
    return html


def build_html():
    toc = build_toc()
    cover = build_cover_hero()
    ch1 = build_ch1()
    ch2 = build_ch2()
    ch3 = build_ch3()
    ch4 = build_ch4()
    ch5 = build_ch5()
    ch6 = build_ch6()
    refs = build_references()

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Science of Science 서베이 보고서</title>
<!-- Open Graph -->
<meta property="og:title" content="과학을 과학하다: 데이터와 AI로 바라본 과학의 구조, 동역학, 그리고 미래" />
<meta property="og:description" content="Science of Science 분야의 주요 연구 동향과 분석 결과를 정리한 보고서입니다." />
<meta property="og:image" content="https://jehyunlee.github.io/science-of-science-review/og-image.png" />
<meta property="og:url" content="https://jehyunlee.github.io/science-of-science-review/" />
<meta property="og:type" content="website" />
<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="과학을 과학하다: 데이터와 AI로 바라본 과학의 구조, 동역학, 그리고 미래" />
<meta name="twitter:description" content="Science of Science 분야의 주요 연구 동향과 분석 결과를 정리한 보고서입니다." />
<meta name="twitter:image" content="https://jehyunlee.github.io/science-of-science-review/og-image.png" />
<style>{CSS}</style>
</head>
<body>
<div id="progress-bar"></div>

<nav id="sidebar">
  <div id="sidebar-header">
    <h2>Science of Science<br>서베이 보고서</h2>
    <p>과학을 과학하다</p>
  </div>
  <div id="toc">{toc}</div>
</nav>

<button id="hamburger">&#9776;</button>

<main id="main">
{cover}
{ch1}
{ch2}
{ch3}
{ch4}
{ch5}
{ch6}
{refs}
<footer>
  <p>Claude Code powered by Oh-My-ClaudeCode (by Yeachan HEO), SKILL by Jehyun LEE | jehyun.lee@gmail.com</p>
  <p>2026.02.28.</p>
</footer>
</main>

<script>{JS}</script>
</body>
</html>"""
    html = inject_section_figures(html)
    return html


if __name__ == '__main__':
    print('Building HTML report...')
    html = build_html()
    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    size_kb = len(html.encode('utf-8')) // 1024
    print(f'Done: {OUT_FILE}')
    print(f'File size: {size_kb} KB')
