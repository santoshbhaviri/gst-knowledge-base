"""Visual finish for the generated Word files: bilingual letterhead with the
"One Nation, One Tax" band, navy section headings, shaded table headers,
running header and page-numbered footer."""
import re, copy
import docx
from docx.shared import Pt, Cm, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT

NAVY = RGBColor(0x1F, 0x38, 0x64)
GREY = RGBColor(0x59, 0x59, 0x59)
SAFFRON, GREEN, NAVYHEX = 'FF9933', '138808', '1F3864'
HINDI_FONT = 'Nirmala UI'
DEVA = re.compile(r'([ऀ-ॿ][ऀ-ॿ\s,.:।-]*)')


def _el(tag, **attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn('w:' + k), str(v))
    return e


def _border(p, side, color, sz, space=1):
    pPr = p._p.get_or_add_pPr()
    bdr = pPr.find(qn('w:pBdr'))
    if bdr is None:
        bdr = _el('w:pBdr'); pPr.append(bdr)
    bdr.append(_el('w:' + side, val='single', sz=sz, space=space, color=color))


def _shade(p, fill):
    p._p.get_or_add_pPr().append(_el('w:shd', val='clear', color='auto', fill=fill))


def _spacing(p, before=0, after=0, line=None):
    pf = p.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    if line:
        pf.line_spacing = line


def _runs(p, text, size, bold=False, color=None, caps=False):
    """Add text, putting Devanagari segments in a Hindi font."""
    for i, seg in enumerate(DEVA.split(text)):
        if not seg:
            continue
        r = p.add_run(seg)
        r.font.size = Pt(size); r.font.bold = bold
        if color is not None:
            r.font.color.rgb = color
        rpr = r._r.get_or_add_rPr()
        rpr.append(_el('w:szCs', val=int(size * 2)))
        if bold:
            rpr.append(_el('w:bCs'))
        if i % 2 == 1:  # Devanagari
            rf = rpr.find(qn('w:rFonts'))
            if rf is None:
                rf = _el('w:rFonts'); rpr.insert(0, rf)
            for a in ('ascii', 'hAnsi', 'cs'):
                rf.set(qn('w:' + a), HINDI_FONT)
            rf.set(qn('w:hint'), 'cs')
    return p


def _new_par_before(anchor_p):
    new = OxmlElement('w:p')
    anchor_p._p.addprevious(new)
    return docx.text.paragraph.Paragraph(new, anchor_p._parent)


def _letterhead(d, o):
    paras = list(d.paragraphs)
    start = next((i for i, p in enumerate(paras) if p.text.strip().startswith('भारत सरकार')), None)
    if start is None:
        return False
    band = next(i for i in range(start, len(paras)) if 'ONE NATION' in paras[i].text)
    anchor = paras[band + 1]
    # R-series registration documents are issued by the Range Superintendent (Circular 223/17/2024-GST)
    rng = 'SUPERINTENDENT' in ' '.join(p.text for p in paras[start:band + 1])
    office_hi = 'केन्द्रीय कर अधीक्षक का कार्यालय' if rng else 'केन्द्रीय कर सहायक आयुक्त का कार्यालय'
    office_en = 'OFFICE OF THE SUPERINTENDENT OF CENTRAL TAX, [        ] RANGE' if rng else 'OFFICE OF THE ASSISTANT COMMISSIONER OF CENTRAL TAX'
    lines = [
        ('भारत सरकार  |  GOVERNMENT OF INDIA', 11, True, NAVY),
        ('वित्त मंत्रालय, राजस्व विभाग  |  MINISTRY OF FINANCE, DEPARTMENT OF REVENUE', 9, False, GREY),
        (office_hi, 11, True, None),
        (office_en, 11.5, True, None),
        (o['DIVISION_CAPS'], 16, True, NAVY),
        (o['COMMRTE_CAPS'], 11, True, NAVY),
        (o['OFFICE_ADDRESS'], 9, False, GREY),
        ('Telephone: %s   |   E-mail: %s' % (o['OFFICE_PHONE'], o['OFFICE_EMAIL']), 9, False, GREY),
    ]
    made = []
    for text, size, bold, color in lines:
        p = _new_par_before(anchor)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        _spacing(p, 0, 0, 1.0)
        _runs(p, text, size, bold, color)
        made.append(p)
    _border(made[0], 'top', SAFFRON, 36, 6)
    made[0].paragraph_format.space_before = Pt(0)
    made[-1].paragraph_format.space_after = Pt(6)
    tag = _new_par_before(anchor)
    tag.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _spacing(tag, 0, 14, 1.0)
    _shade(tag, NAVYHEX)
    _border(tag, 'bottom', GREEN, 36, 0)
    _runs(tag, 'GST  ★  ONE NATION, ONE TAX  ★  जीएसटी: एक राष्ट्र, एक कर', 10.5, True, RGBColor(0xFF, 0xFF, 0xFF))
    for p in paras[start:band + 1]:
        p._p.getparent().remove(p._p)
    return True


def _title_block(d):
    for p in d.paragraphs:
        t = p.text.strip()
        if t.startswith('FORM GST RFD-0'):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for side in ('top', 'left', 'bottom', 'right'):
                _border(p, side, NAVYHEX, 8, 4)
            _shade(p, 'EEF2F8')
            _spacing(p, 4, 10, 1.1)
            for r in p.runs:
                r.font.color.rgb = NAVY
            return


HEAD_RE = re.compile(r'^(\d+[A-Z]?\.|ORDER$|IMPORTANT NOTE|Annexure|Part [A-Z]|Section [A-Z0-9])')


def _headings(d):
    for p in d.paragraphs:
        t = p.text.strip()
        runs = [r for r in p.runs if r.text.strip()]
        if not t or not runs or len(t) > 110:
            continue
        all_bold = all(r.bold for r in runs)
        if p.style.name.startswith('Heading') or (all_bold and HEAD_RE.match(t)):
            for r in p.runs:
                r.font.color.rgb = NAVY
                r.font.size = Pt(12.5)
                r.bold = True
            _spacing(p, 12, 4)
            p.paragraph_format.keep_with_next = True
            _border(p, 'bottom', 'B4C6E7', 6, 1)
            if t.startswith('ORDER') or t.startswith('IMPORTANT NOTE') or re.match(r'^\d+\. ORDER', t):
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER


def _tables(d):
    for t in d.tables:
        tblPr = t._tbl.tblPr
        for b in tblPr.findall(qn('w:tblBorders')):
            tblPr.remove(b)
        borders = _el('w:tblBorders')
        for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
            borders.append(_el('w:' + edge, val='single', sz=4, color='8EA9C1'))
        tblPr.append(borders)
        mar = _el('w:tblCellMar')
        for side, w in (('top', 30), ('bottom', 30), ('left', 80), ('right', 80)):
            mar.append(_el('w:' + side, w=w, type='dxa'))
        tblPr.append(mar)
        if not t.rows:
            continue
        hdr = t.rows[0]
        trPr = hdr._tr.get_or_add_trPr()
        trPr.append(_el('w:tblHeader'))
        two_col_particulars = len(t.columns) == 2 and hdr.cells[0].text.strip() in ('Particulars', 'Component', 'Item')
        for c in hdr.cells:
            c._tc.get_or_add_tcPr().append(_el('w:shd', val='clear', color='auto', fill='DCE6F1'))
            for p in c.paragraphs:
                for r in p.runs:
                    r.bold = True; r.font.color.rgb = NAVY
        for row in t.rows:
            # bold "Total" rows are lightly shaded
            if any(c.text.strip().startswith('Total') for c in row.cells[:3]):
                for c in row.cells:
                    c._tc.get_or_add_tcPr().append(_el('w:shd', val='clear', color='auto', fill='F2F2F2'))
            if two_col_particulars and row is not hdr:
                c0 = row.cells[0]
                c0._tc.get_or_add_tcPr().append(_el('w:shd', val='clear', color='auto', fill='F5F8FC'))
                for p in c0.paragraphs:
                    for r in p.runs:
                        r.bold = True
            small = len(t.columns) >= 7
            for c in row.cells:
                for p in c.paragraphs:
                    _spacing(p, 0, 0, 1.0)
                    if small:
                        for r in p.runs:
                            r.font.size = Pt(9)


def _body(d):
    for p in d.paragraphs:
        if p.style.name in ('Body Text', 'First Paragraph', 'Normal', 'Compact') and p.paragraph_format.space_after is None:
            _spacing(p, 0, 6, 1.12)
        t = p.text.strip()
        if t.startswith('(Signature)'):
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            p.paragraph_format.keep_together = True
            p.paragraph_format.space_before = Pt(24)


def _field(run, instr):
    for kind, extra in (('begin', None), ('instr', instr), ('separate', None), ('end', None)):
        if kind == 'instr':
            it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = extra
            run._r.append(it)
        else:
            run._r.append(_el('w:fldChar', fldCharType=kind))
            if kind == 'separate':
                tx = OxmlElement('w:t'); tx.text = '1'; run._r.append(tx)


def _header_footer(d, o, title, has_letterhead, landscape):
    sec = d.sections[0]
    sec.header_distance = Cm(1.0); sec.footer_distance = Cm(1.0)
    usable = sec.page_width - sec.left_margin - sec.right_margin
    if has_letterhead:
        sec.different_first_page_header_footer = True
    left = '%s, %s' % (o['DIVISION'], o['COMMRTE'])
    is_notice = 'RFD-08' in (title or '') or (title or '').startswith('Template A')   # A-series: SCN-side notices
    kind = 'Notice' if is_notice else 'Order'
    if (title or '').startswith('Template R'):   # R-series: registration; the title says what the document is
        low = title.split(':', 1)[-1].lower()
        kind = 'Report' if 'report' in low else 'Note' if 'recorded reasons' in low else ('Notice' if ('notice' in low or 'query' in low or 'reasons' in low) else 'Order')
    right = ('%s No. [ ] dated [DD.MM.YYYY]' % kind) if has_letterhead else (title or '').split(':')[0]

    hp = sec.header.paragraphs[0]
    hp.text = ''
    hp.paragraph_format.tab_stops.add_tab_stop(usable, WD_TAB_ALIGNMENT.RIGHT)
    for txt in (left, '\t' + right):
        r = hp.add_run(txt); r.font.size = Pt(8.5); r.font.color.rgb = GREY
    _border(hp, 'bottom', 'B4C6E7', 6, 2)

    footers = [sec.footer] + ([sec.first_page_footer] if has_letterhead else [])
    for ft in footers:
        fp = ft.paragraphs[0]
        fp.text = ''
        fp.paragraph_format.tab_stops.add_tab_stop(usable, WD_TAB_ALIGNMENT.RIGHT)
        _border(fp, 'top', SAFFRON, 6, 2)
        r = fp.add_run('GST: One Nation, One Tax'); r.font.size = Pt(8.5); r.font.color.rgb = NAVY; r.bold = True
        r = fp.add_run('\tPage '); r.font.size = Pt(8.5); r.font.color.rgb = GREY
        r = fp.add_run(); r.font.size = Pt(8.5); _field(r, ' PAGE ')
        r = fp.add_run(' of '); r.font.size = Pt(8.5); r.font.color.rgb = GREY
        r = fp.add_run(); r.font.size = Pt(8.5); _field(r, ' NUMPAGES ')


def _move_howto(d):
    for p in d.paragraphs:
        if p.text.strip().startswith('How to use this template.'):
            body = p._p.getparent()
            sect = body.find(qn('w:sectPr'))
            p._p.getparent().remove(p._p)
            if sect is not None:
                sect.addprevious(p._p)
            else:
                body.append(p._p)
            p.paragraph_format.space_before = Pt(18)
            return


def dress(path, title, office):
    d = docx.Document(path)
    if 'RFD-0' in (title or '') or True:
        _move_howto(d)
    has_lh = _letterhead(d, office)
    _title_block(d)
    _headings(d)
    _tables(d)
    _body(d)
    _header_footer(d, office, title, has_lh, 'checklist' in path)
    if title:
        d.core_properties.title = title
    d.core_properties.author = office['DIVISION']
    d.save(path)
