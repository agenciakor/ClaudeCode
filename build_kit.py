#!/usr/bin/env python3
"""Generator for Automatiza World Elementor Template Kit.

Produces a ZIP in the Envato/Template-Kit-Import format used by the
"Envato Elements / Template Kit Import" WordPress plugin and accepted by
Elementor Pro. Structure:

  kit/
    manifest.json   ← templates as ARRAY of entries
    help.html
    templates/{slug}.json
    screenshots/{slug}.jpg
"""
import json
import os
import random
import shutil
import time
import zipfile
from pathlib import Path

random.seed(20260511)

ROOT = Path(__file__).parent
KIT = ROOT / "automatiza-world-elementor-kit"
TPL = KIT / "templates"
SHOTS = KIT / "screenshots"

# ---------- helpers ----------
def uid() -> str:
    return "".join(random.choices("abcdef0123456789", k=8))

def px(top=0, right=0, bottom=0, left=0, linked=False, unit="px"):
    return {"unit": unit, "top": str(top), "right": str(right),
            "bottom": str(bottom), "left": str(left), "isLinked": linked}

def size(n, unit="px"):
    return {"unit": unit, "size": n, "sizes": []}

def section(elements, settings=None, inner=False):
    return {
        "id": uid(),
        "elType": "section",
        "settings": settings or {},
        "elements": elements,
        "isInner": inner,
    }

def column(width, elements, settings=None):
    s = {"_column_size": width, "_inline_size": None}
    if settings:
        s.update(settings)
    return {
        "id": uid(),
        "elType": "column",
        "settings": s,
        "elements": elements,
        "isInner": False,
    }

def widget(wtype, settings):
    return {
        "id": uid(),
        "elType": "widget",
        "widgetType": wtype,
        "settings": settings,
        "elements": [],
    }

# ---------- shared widgets ----------
def eyebrow(text, align="left", delay=0):
    return widget("heading", {
        "title": text,
        "header_size": "p",
        "align": align,
        "title_color": "#F0A500",
        "typography_typography": "custom",
        "typography_font_family": "Inter",
        "typography_font_size": size(11),
        "typography_font_weight": "700",
        "typography_letter_spacing": size(0.08, "em"),
        "typography_text_transform": "uppercase",
        "_animation": "fadeInUp",
        "_animation_delay": delay,
        "_margin": px(0, 0, 8, 0),
    })

def amber_divider(align="left"):
    return widget("divider", {
        "color": "#F0A500",
        "weight": size(3),
        "width": size(50, "%"),
        "align": align,
        "_margin": px(0, 0, 20, 0),
        "gap": size(0),
    })

def heading(text, tag="h2", color="#0D2137", fsize=36, weight="700",
            align="left", anim="fadeInUp", delay=0, margin_b=16):
    return widget("heading", {
        "title": text,
        "header_size": tag,
        "align": align,
        "title_color": color,
        "typography_typography": "custom",
        "typography_font_family": "Inter",
        "typography_font_size": size(fsize),
        "typography_font_weight": weight,
        "typography_line_height": size(1.2, "em"),
        "_animation": anim,
        "_animation_delay": delay,
        "_margin": px(0, 0, margin_b, 0),
    })

def text(content, color="#5A7A8A", fsize=16, align="left",
         anim="fadeInUp", delay=100, margin_b=24):
    return widget("text-editor", {
        "editor": f"<p>{content}</p>",
        "text_color": color,
        "align": align,
        "typography_typography": "custom",
        "typography_font_family": "Inter",
        "typography_font_size": size(fsize),
        "typography_font_weight": "400",
        "typography_line_height": size(1.65, "em"),
        "_animation": anim,
        "_animation_delay": delay,
        "_margin": px(0, 0, margin_b, 0),
    })

def cta_primary(label, link="#contato", align="left", delay=200):
    return widget("button", {
        "text": label,
        "link": {"url": link, "is_external": "", "nofollow": ""},
        "align": align,
        "size": "md",
        "background_color": "#F0A500",
        "button_text_color": "#0D2137",
        "hover_color": "#0D2137",
        "button_background_hover_color": "#FFB733",
        "border_radius": px(4, 4, 4, 4, True),
        "text_padding": px(14, 28, 14, 28),
        "typography_typography": "custom",
        "typography_font_family": "Inter",
        "typography_font_size": size(15),
        "typography_font_weight": "700",
        "_animation": "fadeInUp",
        "_animation_delay": delay,
    })

def cta_outline(label, link="#produtos", align="left", delay=300):
    return widget("button", {
        "text": label,
        "link": {"url": link, "is_external": "", "nofollow": ""},
        "align": align,
        "size": "md",
        "background_color": "rgba(0,0,0,0)",
        "button_text_color": "#0D2137",
        "hover_color": "#0D2137",
        "button_background_hover_color": "#F0A500",
        "border_border": "solid",
        "border_width": px(2, 2, 2, 2, True),
        "border_color": "#F0A500",
        "border_radius": px(4, 4, 4, 4, True),
        "text_padding": px(12, 26, 12, 26),
        "typography_typography": "custom",
        "typography_font_family": "Inter",
        "typography_font_size": size(15),
        "typography_font_weight": "700",
        "_animation": "fadeInUp",
        "_animation_delay": delay,
    })

def spacer(h=40):
    return widget("spacer", {"space": size(h)})

def image_widget(url, alt, delay=200):
    return widget("image", {
        "image": {"url": url, "id": ""},
        "image_size": "full",
        "align": "center",
        "_animation": "fadeInRight",
        "_animation_delay": delay,
        "image_border_radius": px(8, 8, 8, 8, True),
        "_alt": alt,
    })

def icon_box(icon, title, desc, border_left=False, color="#0D2137"):
    s = {
        "selected_icon": {"value": icon, "library": "fa-solid"},
        "title_text": title,
        "description_text": desc,
        "view": "default",
        "position": "left",
        "title_size": "h3",
        "primary_color": "#F0A500",
        "icon_color": "#F0A500",
        "title_color": color,
        "description_color": "#5A7A8A",
        "icon_space": size(16),
        "title_typography_typography": "custom",
        "title_typography_font_family": "Inter",
        "title_typography_font_size": size(18),
        "title_typography_font_weight": "700",
        "description_typography_typography": "custom",
        "description_typography_font_family": "Inter",
        "description_typography_font_size": size(14),
        "description_typography_line_height": size(1.55, "em"),
        "_padding": px(24, 24, 24, 24),
        "_background_background": "classic",
        "_background_color": "#FFFFFF",
        "_border_radius": px(6, 6, 6, 6, True),
        "_animation": "fadeInUp",
    }
    if border_left:
        s["_border_border"] = "solid"
        s["_border_width"] = px(0, 0, 0, 3, False)
        s["_border_color"] = "#F0A500"
    return widget("icon-box", s)

# ---------- backgrounds ----------
def bg_dark():
    return {"background_background": "classic", "background_color": "#0D2137",
            "padding": px(80, 20, 80, 20)}
def bg_navy2():
    return {"background_background": "classic", "background_color": "#081E2E",
            "padding": px(60, 20, 60, 20)}
def bg_light():
    return {"background_background": "classic", "background_color": "#F4F6F9",
            "padding": px(80, 20, 80, 20)}
def bg_white():
    return {"background_background": "classic", "background_color": "#FFFFFF",
            "padding": px(80, 20, 80, 20)}
def bg_amber():
    return {"background_background": "classic", "background_color": "#F0A500",
            "padding": px(70, 20, 70, 20)}

def hero_dark(h1, sub):
    s = bg_dark()
    s["padding"] = px(110, 20, 110, 20)
    return section([
        column(100, [
            eyebrow("AUTOMATIZA WORLD", align="center"),
            widget("divider", {"color": "#F0A500", "weight": size(3),
                               "width": size(60), "align": "center",
                               "_margin": px(0, 0, 24, 0), "gap": size(0)}),
            heading(h1, tag="h1", color="#FFFFFF", fsize=44, align="center",
                    anim="fadeInLeft"),
            text(sub, color="#A8B8C2", fsize=18, align="center", margin_b=0),
        ]),
    ], s)

def cta_bar_amber(h2, sub, btn="Falar com um especialista"):
    return section([
        column(70, [
            heading(h2, tag="h2", color="#0D2137", fsize=32, align="left"),
            text(sub, color="#0D2137", fsize=16, align="left", margin_b=0),
        ]),
        column(30, [
            widget("button", {
                "text": btn,
                "link": {"url": "/contato", "is_external": "", "nofollow": ""},
                "align": "right",
                "size": "md",
                "background_color": "#0D2137",
                "button_text_color": "#F0A500",
                "hover_color": "#F0A500",
                "button_background_hover_color": "#081E2E",
                "border_radius": px(4, 4, 4, 4, True),
                "text_padding": px(16, 32, 16, 32),
                "typography_typography": "custom",
                "typography_font_family": "Inter",
                "typography_font_size": size(15),
                "typography_font_weight": "700",
            }),
        ]),
    ], bg_amber())

# ---------- writers (Envato Template Kit format) ----------
def write_doc(slug: str, title: str, doc_type: str, template_type: str,
              content, page_settings=None, extra_metadata=None,
              extra_info=None):
    """Write a template JSON in the Envato Template Kit format."""
    metadata = {
        "template_type": template_type,
        "include_in_zip": "1",
        "elementor_pro_required": "1",
        "wp_page_template": "default",
    }
    if extra_metadata:
        metadata.update(extra_metadata)
    if extra_info:
        metadata["additional_template_information"] = extra_info
    data = {
        "version": "0.4",
        "title": title,
        "type": doc_type,
        "metadata": metadata,
        "content": content,
    }
    if page_settings is not None:
        data["page_settings"] = page_settings
    p = TPL / f"{slug}.json"
    p.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    json.loads(p.read_text(encoding="utf-8"))

# ============================================================
# templates/global.json (kit theme styles)
# ============================================================
def build_global():
    page_settings = {
        "system_colors": [
            {"_id": "primary", "title": "Primary", "color": "#0D2137"},
            {"_id": "secondary", "title": "Secondary", "color": "#081E2E"},
            {"_id": "text", "title": "Text", "color": "#5A7A8A"},
            {"_id": "accent", "title": "Accent", "color": "#F0A500"},
        ],
        "custom_colors": [
            {"_id": "aw_amber", "title": "AW Amber", "color": "#F0A500"},
            {"_id": "aw_dark", "title": "AW Dark", "color": "#0D2137"},
            {"_id": "aw_navy2", "title": "AW Navy 2", "color": "#081E2E"},
            {"_id": "aw_light", "title": "AW Light", "color": "#F4F6F9"},
            {"_id": "aw_white", "title": "AW White", "color": "#FFFFFF"},
            {"_id": "aw_text", "title": "AW Text Muted", "color": "#5A7A8A"},
            {"_id": "aw_border", "title": "AW Border", "color": "#E1E7ED"},
        ],
        "system_typography": [
            {"_id": "primary", "title": "H1 Heading",
             "typography_typography": "custom",
             "typography_font_family": "Inter",
             "typography_font_weight": "700",
             "typography_font_size": size(48),
             "typography_line_height": size(1.2, "em")},
            {"_id": "secondary", "title": "H2 Heading",
             "typography_typography": "custom",
             "typography_font_family": "Inter",
             "typography_font_weight": "700",
             "typography_font_size": size(36),
             "typography_line_height": size(1.2, "em")},
            {"_id": "text", "title": "H3 Heading",
             "typography_typography": "custom",
             "typography_font_family": "Inter",
             "typography_font_weight": "600",
             "typography_font_size": size(24),
             "typography_line_height": size(1.3, "em")},
            {"_id": "accent", "title": "Body",
             "typography_typography": "custom",
             "typography_font_family": "Inter",
             "typography_font_weight": "400",
             "typography_font_size": size(16),
             "typography_line_height": size(1.65, "em")},
        ],
        "custom_typography": [],
        "default_generic_fonts": "Sans-serif",
        "page_title_selector": "h1.entry-title",
        "activeItemIndex": 1,
        "viewport_md": 768,
        "viewport_lg": 1025,
        "button_border_radius": px(4, 4, 4, 4, True),
        "button_padding": px(14, 28, 14, 28),
        "button_text_color": "#0D2137",
        "button_background_color": "#F0A500",
        "button_hover_text_color": "#0D2137",
        "button_hover_background_color": "#FFB733",
        "form_field_border_border": "solid",
        "form_field_border_width": px(1, 1, 1, 1, True),
        "form_field_padding": px(12, 16, 12, 16),
        "form_field_border_radius": px(4, 4, 4, 4, True),
        "hello_footer_copyright_text": "© Automatiza World — Todos os direitos reservados",
    }
    write_doc(
        slug="global",
        title="Global Kit Styles",
        doc_type="section",
        template_type="global-styles",
        content=[],
        page_settings=page_settings,
        extra_info=["These are the global theme styles configured through "
                    "the Elementor Theme Styles area."],
    )

# ============================================================
# header
# ============================================================
def build_header():
    nav_settings = {
        "menu": "primary",
        "layout": "horizontal",
        "align": "right",
        "menu_typography_typography": "custom",
        "menu_typography_font_family": "Inter",
        "menu_typography_font_size": size(14),
        "menu_typography_font_weight": "600",
        "color_menu_item": "#FFFFFF",
        "color_menu_item_hover": "#F0A500",
        "color_menu_item_active": "#F0A500",
        "menu_space_between": size(28),
    }
    sec = section([
        column(20, [
            widget("image", {
                "image": {"url": "{{LOGO_URL}}", "id": ""},
                "image_size": "full",
                "align": "left",
                "width": size(180),
                "_alt": "Automatiza World - Ensacadeiras automáticas industriais",
            }),
        ]),
        column(60, [widget("nav-menu", nav_settings)]),
        column(20, [
            cta_primary("Solicitar orçamento", link="/contato",
                        align="right", delay=0),
        ]),
    ], {
        "background_background": "classic",
        "background_color": "#0D2137",
        "padding": px(16, 32, 16, 32),
        "structure": "30",
        "stretch_section": "section-stretched",
    })
    write_doc(
        slug="header",
        title="Header",
        doc_type="header",
        template_type="section-header",
        content=[sec],
        page_settings={"content_wrapper_html_tag": "div"},
        extra_metadata={
            "elementor_library_type": "header",
            "elementor_pro_conditions": ["include/general"],
        },
        extra_info=[
            "This is a \"Header\" template for Elementor Pro.",
            "This template will display on: Entire Site.",
        ],
    )

# ============================================================
# footer
# ============================================================
def build_footer():
    main = section([
        column(35, [
            widget("image", {
                "image": {"url": "{{LOGO_URL}}", "id": ""},
                "image_size": "full",
                "align": "left",
                "width": size(160),
                "_alt": "Automatiza World",
            }),
            spacer(20),
            text("Fabricante brasileira de ensacadeiras automáticas industriais. "
                 "Mais de 20 anos automatizando processos para indústrias de "
                 "ração, soja, fertilizantes, química e mineração.",
                 color="#A8B8C2", fsize=14, margin_b=24),
            widget("icon-list", {
                "view": "traditional",
                "icon_list": [
                    {"_id": uid(), "text": "(11) 4000-0000",
                     "selected_icon": {"value": "fas fa-phone", "library": "fa-solid"},
                     "link": {"url": "tel:+551140000000"}},
                    {"_id": uid(), "text": "comercial@automatizaworld.com.br",
                     "selected_icon": {"value": "fas fa-envelope", "library": "fa-solid"},
                     "link": {"url": "mailto:comercial@automatizaworld.com.br"}},
                    {"_id": uid(), "text": "WhatsApp comercial",
                     "selected_icon": {"value": "fab fa-whatsapp", "library": "fa-brands"},
                     "link": {"url": "https://wa.me/5511900000000"}},
                ],
                "icon_color": "#F0A500",
                "text_color": "#A8B8C2",
                "text_typography_typography": "custom",
                "text_typography_font_family": "Inter",
                "text_typography_font_size": size(14),
                "space_between": size(12),
            }),
        ]),
        column(20, [
            heading("Produtos", tag="h4", color="#FFFFFF", fsize=16, margin_b=20),
            widget("icon-list", {
                "view": "traditional",
                "icon_list": [
                    {"_id": uid(), "text": "Ensacadeiras de sopro",
                     "selected_icon": {"value": "", "library": ""},
                     "link": {"url": "/ensacadeiras#sopro"}},
                    {"_id": uid(), "text": "Ensacadeiras gravimétricas",
                     "selected_icon": {"value": "", "library": ""},
                     "link": {"url": "/ensacadeiras#gravimetrica"}},
                    {"_id": uid(), "text": "Ensacadeiras big bag",
                     "selected_icon": {"value": "", "library": ""},
                     "link": {"url": "/ensacadeiras#bigbag"}},
                    {"_id": uid(), "text": "Roscas transportadoras",
                     "selected_icon": {"value": "", "library": ""},
                     "link": {"url": "/ensacadeiras#rosca"}},
                    {"_id": uid(), "text": "Ver todos os modelos",
                     "selected_icon": {"value": "", "library": ""},
                     "link": {"url": "/ensacadeiras"}},
                ],
                "text_color": "#A8B8C2",
                "text_typography_typography": "custom",
                "text_typography_font_family": "Inter",
                "text_typography_font_size": size(14),
                "space_between": size(10),
            }),
        ]),
        column(20, [
            heading("Empresa", tag="h4", color="#FFFFFF", fsize=16, margin_b=20),
            widget("icon-list", {
                "view": "traditional",
                "icon_list": [
                    {"_id": uid(), "text": "Sobre a Automatiza",
                     "selected_icon": {"value": "", "library": ""},
                     "link": {"url": "/sobre"}},
                    {"_id": uid(), "text": "Segmentos atendidos",
                     "selected_icon": {"value": "", "library": ""},
                     "link": {"url": "/segmentos"}},
                    {"_id": uid(), "text": "Serviços e suporte",
                     "selected_icon": {"value": "", "library": ""},
                     "link": {"url": "/servicos"}},
                    {"_id": uid(), "text": "Blog técnico",
                     "selected_icon": {"value": "", "library": ""},
                     "link": {"url": "/blog"}},
                    {"_id": uid(), "text": "Trabalhe conosco",
                     "selected_icon": {"value": "", "library": ""},
                     "link": {"url": "/sobre#carreiras"}},
                ],
                "text_color": "#A8B8C2",
                "text_typography_typography": "custom",
                "text_typography_font_family": "Inter",
                "text_typography_font_size": size(14),
                "space_between": size(10),
            }),
        ]),
        column(25, [
            heading("Contato", tag="h4", color="#FFFFFF", fsize=16, margin_b=20),
            text("Av. Industrial, 1234 — Galpão 8<br>"
                 "Distrito Industrial — São Paulo / SP<br>CEP 00000-000",
                 color="#A8B8C2", fsize=14, margin_b=24),
            text("<strong style='color:#F0A500;'>Linha de financiamento BNDES disponível.</strong>",
                 color="#A8B8C2", fsize=13, margin_b=0),
        ]),
    ], {
        "background_background": "classic",
        "background_color": "#0D2137",
        "padding": px(70, 20, 50, 20),
        "structure": "33",
    })
    bottom = section([
        column(50, [
            text("© 2026 Automatiza World — Todos os direitos reservados",
                 color="#5A7A8A", fsize=13, align="left", margin_b=0),
        ]),
        column(50, [
            text('<a href="/politica-de-privacidade" style="color:#5A7A8A;">'
                 'Política de Privacidade</a> &nbsp;|&nbsp; '
                 '<a href="/termos" style="color:#5A7A8A;">Termos de Uso</a>',
                 color="#5A7A8A", fsize=13, align="right", margin_b=0),
        ]),
    ], {
        "background_background": "classic",
        "background_color": "#060F17",
        "padding": px(20, 20, 20, 20),
    })
    write_doc(
        slug="footer",
        title="Footer",
        doc_type="footer",
        template_type="section-footer",
        content=[main, bottom],
        page_settings={"content_wrapper_html_tag": "div"},
        extra_metadata={
            "elementor_library_type": "footer",
            "elementor_pro_conditions": ["include/general"],
        },
        extra_info=[
            "This is a \"Footer\" template for Elementor Pro.",
            "This template will display on: Entire Site.",
        ],
    )

# ============================================================
# home
# ============================================================
def build_home():
    hero = section([
        column(55, [
            eyebrow("TECNOLOGIA EM ENSAQUE INDUSTRIAL"),
            amber_divider(),
            heading("Ensacadeiras automáticas para indústrias que não param",
                    tag="h1", fsize=48, anim="fadeInLeft"),
            text("Soluções de alta performance para fábricas de ração, "
                 "produtores de soja, fertilizantes e toda indústria que "
                 "precisa de precisão e velocidade em escala.", fsize=18,
                 margin_b=32),
            section([
                column(50, [cta_primary("Solicitar orçamento", "/contato")]),
                column(50, [cta_outline("Ver produtos", "/ensacadeiras")]),
            ], {"padding": px(0, 0, 0, 0)}, inner=True),
        ]),
        column(45, [
            image_widget(
                "https://images.unsplash.com/photo-1565043666747-69f6646db940?w=800&q=80",
                "Linha de produção industrial automatizada com ensacadeira"),
        ]),
    ], {**bg_light(), "padding": px(110, 20, 110, 20), "structure": "5545"})

    def trust(num, label):
        return column(25, [
            heading(num, tag="h3", color="#F0A500", fsize=42, align="center", margin_b=8),
            text(label, color="#FFFFFF", fsize=14, align="center", margin_b=0),
        ])
    trust_bar = section([
        trust("+20 anos", "de mercado"),
        trust("+300", "indústrias atendidas"),
        trust("8 modelos", "de ensacadeiras"),
        trust("100%", "fabricação nacional"),
    ], {**bg_navy2(), "structure": "44"})

    prod_header = section([
        column(100, [
            eyebrow("LINHA DE PRODUTOS", align="center"),
            amber_divider(align="center"),
            heading("Ensacadeiras para cada processo industrial",
                    tag="h2", fsize=36, align="center", margin_b=0),
        ]),
    ], {**bg_white(), "padding": px(80, 20, 30, 20)})

    def prod_card(tag, title, desc):
        return column(33, [
            widget("heading", {
                "title": tag, "header_size": "p",
                "title_color": "#0D2137",
                "_background_background": "classic",
                "_background_color": "#F0A500",
                "_padding": px(6, 12, 6, 12),
                "typography_typography": "custom",
                "typography_font_family": "Inter",
                "typography_font_size": size(11),
                "typography_font_weight": "700",
                "typography_text_transform": "uppercase",
                "typography_letter_spacing": size(0.05, "em"),
                "_margin": px(0, 0, 16, 0),
                "align": "left",
            }),
            heading(title, tag="h3", fsize=22, margin_b=12),
            text(desc, fsize=14, margin_b=20),
            widget("button", {
                "text": "Ver modelos →",
                "link": {"url": "/ensacadeiras", "is_external": ""},
                "align": "left", "size": "sm",
                "background_color": "rgba(0,0,0,0)",
                "button_text_color": "#F0A500",
                "border_radius": px(0, 0, 0, 0, True),
                "text_padding": px(0, 0, 0, 0),
                "typography_typography": "custom",
                "typography_font_family": "Inter",
                "typography_font_size": size(14),
                "typography_font_weight": "700",
            }),
        ], {
            "background_background": "classic",
            "background_color": "#FFFFFF",
            "border_border": "solid",
            "border_width": px(1, 1, 1, 1, True),
            "border_color": "#E1E7ED",
            "border_radius": px(8, 8, 8, 8, True),
            "padding": px(28, 28, 28, 28),
            "margin": px(10, 10, 10, 10),
        })
    prod_cards = section([
        prod_card("SOPRO", "Ensacadeiras de sopro",
                  "Ideais para produtos pulverulentos com alta produtividade. "
                  "Ensaque rápido em sacos válvula com selagem precisa."),
        prod_card("GRAVIMÉTRICA", "Ensacadeiras gravimétricas",
                  "Precisão de pesagem para produtos granulados. "
                  "Atendem normas Inmetro/CONMETRO com células de carga calibradas."),
        prod_card("BIG BAG", "Ensacadeiras big bag",
                  "Para volumes de 500 a 1500 kg. Estrutura robusta "
                  "com ganchos pneumáticos e enchimento controlado."),
    ], {**bg_white(), "padding": px(20, 20, 80, 20), "structure": "33"})

    seg_header = section([
        column(100, [
            eyebrow("SEGMENTOS ATENDIDOS", align="center"),
            amber_divider(align="center"),
            heading("Indústrias que confiam na Automatiza World",
                    tag="h2", fsize=36, align="center", margin_b=0),
        ]),
    ], {**bg_light(), "padding": px(80, 20, 30, 20)})

    def seg_card(icon, title, desc):
        return column(50, [icon_box(icon, title, desc, border_left=True)],
                      {"padding": px(10, 10, 10, 10)})

    seg_grid = section([
        seg_card("fas fa-wheat-awn", "Fábricas de ração animal",
                 "Linhas de ensaque para ração extrusada e farelada com "
                 "controle de poeira e desempenho contínuo."),
        seg_card("fas fa-seedling", "Produtores de soja e grãos",
                 "Ensaque de soja, milho e farelos em sacos válvula ou "
                 "big bag para exportação e mercado interno."),
        seg_card("fas fa-flask", "Indústria de fertilizantes",
                 "Equipamentos resistentes a produtos corrosivos com "
                 "selagem hermética para NPK, ureia e adubos."),
        seg_card("fas fa-mountain", "Química e mineração",
                 "Ensaque de calcário, cimento e produtos químicos "
                 "com sistemas anti-explosão e exaustão integrada."),
    ], {**bg_light(), "padding": px(20, 20, 80, 20), "structure": "22"})

    proc_header = section([
        column(100, [
            eyebrow("COMO TRABALHAMOS", align="center"),
            amber_divider(align="center"),
            heading("Processo em 4 etapas até a operação",
                    tag="h2", fsize=36, align="center", margin_b=0),
        ]),
    ], {**bg_white(), "padding": px(80, 20, 30, 20)})

    def step(num, title, desc):
        return column(25, [
            heading(num, tag="span", color="#F0A500", fsize=56, margin_b=8),
            heading(title, tag="h3", fsize=18, margin_b=12),
            text(desc, fsize=14, margin_b=0),
        ], {"padding": px(20, 20, 20, 20)})

    proc_steps = section([
        step("01", "Diagnóstico técnico",
             "Visita à planta e levantamento das necessidades de ensaque."),
        step("02", "Proposta comercial",
             "Especificação técnica detalhada com prazos e financiamento BNDES."),
        step("03", "Fabricação nacional",
             "Produção em nossa fábrica em São Paulo com controle de qualidade."),
        step("04", "Instalação e suporte",
             "Comissionamento, treinamento operacional e pós-venda dedicado."),
    ], {**bg_white(), "padding": px(20, 20, 80, 20), "structure": "44"})

    cta_bar = cta_bar_amber(
        "Pronto para automatizar seu processo de ensaque?",
        "Solicite um diagnóstico técnico gratuito e descubra a ensacadeira "
        "ideal para sua produção.")

    write_doc(
        slug="home",
        title="Home",
        doc_type="section",
        template_type="single-home",
        content=[hero, trust_bar, prod_header, prod_cards,
                 seg_header, seg_grid, proc_header, proc_steps, cta_bar],
        page_settings={"hide_title": "yes"},
    )

# ============================================================
# sobre
# ============================================================
def build_sobre():
    hero = hero_dark(
        "Mais de 20 anos automatizando indústrias brasileiras",
        "Engenharia nacional, suporte próximo e soluções sob medida "
        "para cada processo de ensaque.")
    historia = section([
        column(48, [image_widget(
            "https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800&q=80",
            "Fábrica da Automatiza World - linha de produção")]),
        column(52, [
            eyebrow("NOSSA HISTÓRIA"),
            amber_divider(),
            heading("Da bancada à fábrica de referência nacional",
                    tag="h2", fsize=32, margin_b=20),
            text("Fundada em 2004, a Automatiza World nasceu da necessidade "
                 "de oferecer ao mercado brasileiro ensacadeiras automáticas "
                 "com qualidade de importado e suporte de fabricante nacional.",
                 fsize=16),
            text("Hoje, somos referência no segmento, atendendo mais de 300 "
                 "indústrias em todo o país — de fábricas de ração no Sul a "
                 "mineradoras em Minas Gerais, passando por produtores de soja "
                 "do Centro-Oeste e indústrias químicas do Sudeste.", fsize=16),
            text("Nossa missão é simples: aumentar a produtividade de quem "
                 "produz, com tecnologia robusta, fabricação nacional e "
                 "suporte técnico que responde rápido.", fsize=16, margin_b=0),
        ]),
    ], {**bg_white(), "structure": "4852", "padding": px(80, 20, 80, 20)})
    dif_header = section([
        column(100, [
            eyebrow("POR QUE AUTOMATIZA WORLD", align="center"),
            amber_divider(align="center"),
            heading("Nossos diferenciais", tag="h2", color="#FFFFFF",
                    fsize=36, align="center", margin_b=0),
        ]),
    ], {**bg_dark(), "padding": px(80, 20, 30, 20)})

    def dif_box(icon, title, desc):
        return column(25, [
            widget("icon-box", {
                "selected_icon": {"value": icon, "library": "fa-solid"},
                "title_text": title, "description_text": desc,
                "view": "default", "position": "top", "title_size": "h3",
                "primary_color": "#F0A500",
                "title_color": "#FFFFFF",
                "description_color": "#A8B8C2",
                "icon_size": size(40),
                "icon_space": size(20),
                "title_typography_typography": "custom",
                "title_typography_font_family": "Inter",
                "title_typography_font_size": size(18),
                "title_typography_font_weight": "700",
                "description_typography_typography": "custom",
                "description_typography_font_family": "Inter",
                "description_typography_font_size": size(14),
                "description_typography_line_height": size(1.6, "em"),
                "_padding": px(20, 20, 20, 20),
            }),
        ], {"padding": px(10, 10, 10, 10)})

    dif_grid = section([
        dif_box("fas fa-drafting-compass", "Engenharia sob medida",
                "Cada projeto é dimensionado para o produto, fluxo e layout "
                "específicos da sua planta."),
        dif_box("fas fa-industry", "Fabricação nacional",
                "100% produzido no Brasil, com peças disponíveis e prazos "
                "muito menores que importados."),
        dif_box("fas fa-headset", "Suporte técnico próximo",
                "Equipe técnica em todo o território nacional, com atendimento "
                "remoto 24h e visitas programadas."),
        dif_box("fas fa-bolt", "Máxima produtividade",
                "Equipamentos com até 1.200 sacos/h e disponibilidade superior "
                "a 98% em operação contínua."),
    ], {**bg_dark(), "padding": px(20, 20, 80, 20), "structure": "44"})
    cta = cta_bar_amber("Vamos conversar sobre o seu projeto?",
                        "Equipe comercial e engenharia prontos para entender sua "
                        "necessidade e propor a solução ideal.")
    write_doc(
        slug="sobre", title="Sobre",
        doc_type="page", template_type="single-page",
        content=[hero, historia, dif_header, dif_grid, cta],
        page_settings={"hide_title": "yes"},
    )

# ============================================================
# ensacadeiras
# ============================================================
def build_ensacadeiras():
    hero = hero_dark("Ensacadeiras automáticas industriais",
                     "Linha completa para cada tipo de produto, saco e produtividade. "
                     "Conheça os modelos da Automatiza World.")

    def specs_list(items):
        return widget("icon-list", {
            "view": "traditional",
            "icon_list": [
                {"_id": uid(), "text": f"<strong>{k}:</strong> {v}",
                 "selected_icon": {"value": "fas fa-check", "library": "fa-solid"},
                 "link": {"url": ""}}
                for k, v in items
            ],
            "icon_color": "#F0A500",
            "text_color": "#0D2137",
            "text_typography_typography": "custom",
            "text_typography_font_family": "Inter",
            "text_typography_font_size": size(15),
            "space_between": size(10),
        })

    def model_block(eb, title, specs, desc, image, image_alt, light_bg, image_left=False):
        bg = bg_light() if light_bg else bg_white()
        bg["padding"] = px(80, 20, 80, 20)
        text_col = column(55, [
            eyebrow(eb), amber_divider(),
            heading(title, tag="h2", fsize=32, margin_b=20),
            specs_list(specs), spacer(20),
            text(desc, fsize=15),
            cta_primary("Solicitar orçamento", "/contato"),
        ])
        img_col = column(45, [image_widget(image, image_alt)])
        cols = [img_col, text_col] if image_left else [text_col, img_col]
        struct = "4555" if image_left else "5545"
        return section(cols, {**bg, "structure": struct})

    sopro = model_block(
        "MODELO AW-SP", "AW-SP — Ensacadeiras de sopro",
        [("Capacidade", "até 1.200 sacos/h"),
         ("Peso por saco", "10 a 50 kg"),
         ("Produto", "pulverulentos (cimento, calcário, farinhas)"),
         ("Tipo de saco", "válvula"),
         ("Acionamento", "pneumático com soprador centrífugo")],
        "Linha de ensacadeiras de sopro projetada para alta cadência em "
        "produtos pulverulentos. Sistema de selagem por pinçamento garante "
        "ensaque limpo e sem vazamentos, com baixíssima geração de poeira "
        "no entorno da máquina.",
        "https://images.unsplash.com/photo-1567789884554-0b844b597180?w=800&q=80",
        "Ensacadeira de sopro AW-SP em operação", light_bg=False)
    grav = model_block(
        "MODELO AW-GV", "AW-GV — Ensacadeiras gravimétricas",
        [("Capacidade", "até 900 sacos/h"),
         ("Precisão", "± 30 g em sacos de 25 kg"),
         ("Peso por saco", "5 a 50 kg"),
         ("Produto", "granulados e farelos"),
         ("Normas", "Inmetro / CONMETRO")],
        "Modelo gravimétrico com células de carga calibradas e dosagem em "
        "duas velocidades. Ideal para produtos com exigência fiscal de "
        "peso, como ração, fertilizantes, sementes e farelos.",
        "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=800&q=80",
        "Ensacadeira gravimétrica AW-GV com pesagem digital",
        light_bg=True, image_left=True)
    bigbag = model_block(
        "MODELO AW-BB", "AW-BB — Ensacadeiras big bag",
        [("Capacidade", "até 30 big bags/h"),
         ("Peso por bag", "500 a 1500 kg"),
         ("Produto", "granulados, pulverulentos e fibrosos"),
         ("Estrutura", "aço carbono pintado ou inox"),
         ("Alimentação", "rosca dosadora ou válvula rotativa")],
        "Estação de ensaque big bag com ganchos pneumáticos, plataforma de "
        "pesagem integrada e sistema de aeração para densificação do "
        "produto. Construção robusta para operação 24/7.",
        "https://images.unsplash.com/photo-1581090700227-1e37b190418e?w=800&q=80",
        "Ensacadeira big bag AW-BB com plataforma de pesagem", light_bg=False)
    final = section([
        column(100, [
            heading("Não encontrou o modelo ideal?", tag="h2", fsize=32,
                    align="center", margin_b=16),
            text("Nossa engenharia desenvolve soluções sob medida para "
                 "produtos especiais, layouts complexos e produtividades "
                 "específicas. Solicite um diagnóstico técnico.",
                 fsize=16, align="center", margin_b=32),
            widget("button", {
                "text": "Agendar diagnóstico técnico",
                "link": {"url": "/contato", "is_external": ""},
                "align": "center", "size": "md",
                "background_color": "#F0A500", "button_text_color": "#0D2137",
                "border_radius": px(4, 4, 4, 4, True),
                "text_padding": px(16, 32, 16, 32),
                "typography_typography": "custom",
                "typography_font_family": "Inter",
                "typography_font_size": size(15),
                "typography_font_weight": "700",
            }),
        ]),
    ], {**bg_light(), "padding": px(80, 20, 80, 20)})
    write_doc(
        slug="ensacadeiras", title="Ensacadeiras",
        doc_type="page", template_type="single-page",
        content=[hero, sopro, grav, bigbag, final],
        page_settings={"hide_title": "yes"},
    )

# ============================================================
# segmentos
# ============================================================
def build_segmentos():
    hero = hero_dark("Soluções de ensaque para cada segmento industrial",
                     "Conheça as configurações desenvolvidas pela Automatiza World "
                     "para os principais setores produtivos do Brasil.")

    def seg_block(eb, title, kw, desc, image, image_alt, light, image_left):
        bg = bg_light() if light else bg_white()
        bg["padding"] = px(80, 20, 80, 20)
        text_col = column(55, [
            eyebrow(eb), amber_divider(),
            heading(title, tag="h2", fsize=32, margin_b=16),
            text(f"<em>Palavras-chave: {kw}</em>", color="#0D2137",
                 fsize=14, margin_b=20),
            text(desc, fsize=16, margin_b=24),
            cta_primary("Solicitar proposta", "/contato"),
        ])
        img_col = column(45, [image_widget(image, image_alt)])
        cols = [img_col, text_col] if image_left else [text_col, img_col]
        struct = "4555" if image_left else "5545"
        return section(cols, {**bg, "structure": struct})

    racao = seg_block(
        "FÁBRICAS DE RAÇÃO ANIMAL",
        "Ensacadeira para ração com alta cadência",
        "ensacadeira para ração, ensaque automático ração, ensacadeira ração animal",
        "Ensacadeiras gravimétricas e de sopro projetadas para ração extrusada "
        "e farelada, com sistema anti-poeira e selagem por costura. Atendemos "
        "fábricas de ração para aves, suínos, bovinos, peixes e pets, com "
        "linhas que vão de 600 a 1.200 sacos por hora.",
        "https://images.unsplash.com/photo-1518915842-b94e0b67c4d4?w=800&q=80",
        "Ensacadeira automática para ração animal",
        light=False, image_left=False)
    soja = seg_block(
        "PRODUTORES DE SOJA E GRÃOS",
        "Ensacadeira para soja e ensaque de grãos",
        "ensacadeira para soja, ensaque de grãos, big bag para soja",
        "Soluções para ensaque de soja, milho, sorgo e farelos em sacos "
        "convencionais ou big bag. Linha big bag AW-BB é a preferida de "
        "exportadores e cooperativas pela robustez, ganchos pneumáticos e "
        "compatibilidade com empilhadeiras de grande porte.",
        "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=800&q=80",
        "Ensaque de soja em big bag", light=True, image_left=True)
    fert = seg_block(
        "INDÚSTRIA DE FERTILIZANTES",
        "Ensacadeira para fertilizante e ensaque de adubo",
        "ensacadeira para fertilizante, ensaque de adubo, ensacadeira NPK",
        "Equipamentos com componentes resistentes à corrosão (inox 304/316) e "
        "selagem hermética para preservar fertilizantes higroscópicos como "
        "ureia, NPK, sulfato de amônio e adubos formulados. Disponível com "
        "exaustão integrada para controle de pó.",
        "https://images.unsplash.com/photo-1625246333195-78d9c38ad449?w=800&q=80",
        "Ensaque de fertilizante NPK em saco válvula",
        light=False, image_left=False)
    quim = seg_block(
        "QUÍMICA E MINERAÇÃO",
        "Ensacadeira para mineração e ensaque de calcário",
        "ensacadeira para mineração, ensaque de calcário, ensaque de cimento",
        "Linhas de ensaque para calcário, cimento, gesso, areia industrial e "
        "produtos químicos. Sistemas com classificação ATEX para áreas com "
        "risco de explosão, exaustão centralizada e construção em aço carbono "
        "pintado ou inox conforme o produto.",
        "https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800&q=80",
        "Ensacadeira para indústria química e mineração",
        light=True, image_left=True)
    cta = cta_bar_amber("Seu segmento exige uma solução específica?",
                        "Conte para nossa engenharia o produto, a cadência desejada e o "
                        "tipo de saco — propomos a configuração ideal.")
    write_doc(
        slug="segmentos", title="Segmentos",
        doc_type="page", template_type="single-page",
        content=[hero, racao, soja, fert, quim, cta],
        page_settings={"hide_title": "yes"},
    )

# ============================================================
# servicos
# ============================================================
def build_servicos():
    hero = hero_dark("Mais que equipamentos — suporte técnico completo",
                     "Instalação, manutenção, peças e treinamento. Tudo para que sua "
                     "ensacadeira opere com máxima disponibilidade.")

    def serv_card(icon, title, desc):
        return column(50, [icon_box(icon, title, desc)],
                      {"padding": px(10, 10, 10, 10)})

    serv_grid = section([
        serv_card("fas fa-screwdriver-wrench", "Instalação e comissionamento",
                  "Equipe técnica especializada para instalação no seu site, "
                  "com testes operacionais e ajuste fino dos parâmetros de "
                  "ensaque até a aceitação final."),
        serv_card("fas fa-shield-halved", "Manutenção preventiva",
                  "Contratos de manutenção preventiva com visitas programadas "
                  "e relatório técnico, evitando paradas não planejadas em "
                  "campanhas críticas."),
        serv_card("fas fa-gears", "Peças de reposição",
                  "Estoque nacional de peças originais com pronta entrega em "
                  "todo o Brasil. Componentes críticos disponíveis em até 48h."),
        serv_card("fas fa-graduation-cap", "Treinamento operacional",
                  "Capacitamos sua equipe operacional e de manutenção, "
                  "presencialmente ou EAD, com material didático e certificado."),
    ], {**bg_light(), "padding": px(80, 20, 80, 20), "structure": "22"})

    proc_header = section([
        column(100, [
            eyebrow("FLUXO DE ATENDIMENTO", align="center"),
            amber_divider(align="center"),
            heading("Da abertura do chamado à resolução",
                    tag="h2", fsize=36, align="center", margin_b=0),
        ]),
    ], {**bg_white(), "padding": px(80, 20, 30, 20)})

    def step(num, title, desc):
        return column(25, [
            heading(num, tag="span", color="#F0A500", fsize=56, margin_b=8),
            heading(title, tag="h3", fsize=18, margin_b=12),
            text(desc, fsize=14, margin_b=0),
        ], {"padding": px(20, 20, 20, 20)})

    proc = section([
        step("01", "Contato",
             "Cliente abre chamado via portal, telefone ou WhatsApp técnico."),
        step("02", "Diagnóstico",
             "Análise remota do problema com nosso time de engenharia."),
        step("03", "Proposta",
             "Plano de ação com prazo, custo e disponibilidade de peças."),
        step("04", "Resolução",
             "Atendimento presencial ou remoto com relatório técnico final."),
    ], {**bg_white(), "padding": px(20, 20, 80, 20), "structure": "44"})
    cta = cta_bar_amber("Sua ensacadeira merece suporte de fabricante.",
                        "Saia do conserto reativo e adote o plano de manutenção da "
                        "Automatiza World.")
    write_doc(
        slug="servicos", title="Serviços",
        doc_type="page", template_type="single-page",
        content=[hero, serv_grid, proc_header, proc, cta],
        page_settings={"hide_title": "yes"},
    )

# ============================================================
# blog
# ============================================================
def build_blog():
    hero = hero_dark("Conteúdo especializado em automação de ensaque",
                     "Guias técnicos, comparativos de modelos e boas práticas para "
                     "indústrias de ração, soja, fertilizantes e mineração.")

    def article_card(cat, date, title, excerpt, image, alt):
        return column(33, [
            widget("image", {
                "image": {"url": image, "id": ""},
                "image_size": "full",
                "_alt": alt,
                "image_border_radius": px(8, 8, 0, 0, False),
            }),
            widget("text-editor", {
                "editor": f'<span style="color:#F0A500;font-size:12px;font-weight:700;'
                          f'text-transform:uppercase;letter-spacing:0.05em;">{cat}</span>'
                          f' &nbsp; <span style="color:#5A7A8A;font-size:12px;">{date}</span>',
                "_padding": px(20, 20, 0, 20),
                "_margin": px(0, 0, 12, 0),
            }),
            widget("heading", {
                "title": title, "header_size": "h3",
                "title_color": "#0D2137",
                "typography_typography": "custom",
                "typography_font_family": "Inter",
                "typography_font_size": size(18),
                "typography_font_weight": "700",
                "typography_line_height": size(1.35, "em"),
                "_padding": px(0, 20, 0, 20),
                "_margin": px(0, 0, 12, 0),
            }),
            widget("text-editor", {
                "editor": f"<p>{excerpt}</p>",
                "text_color": "#5A7A8A",
                "typography_typography": "custom",
                "typography_font_family": "Inter",
                "typography_font_size": size(14),
                "typography_line_height": size(1.6, "em"),
                "_padding": px(0, 20, 16, 20),
            }),
            widget("button", {
                "text": "Ler artigo →",
                "link": {"url": "#", "is_external": ""},
                "align": "left", "size": "sm",
                "background_color": "rgba(0,0,0,0)",
                "button_text_color": "#F0A500",
                "border_radius": px(0, 0, 0, 0, True),
                "text_padding": px(0, 20, 24, 20),
                "typography_typography": "custom",
                "typography_font_family": "Inter",
                "typography_font_size": size(14),
                "typography_font_weight": "700",
            }),
        ], {
            "background_background": "classic",
            "background_color": "#FFFFFF",
            "border_radius": px(8, 8, 8, 8, True),
            "margin": px(10, 10, 10, 10),
            "padding": px(0, 0, 0, 0),
        })

    grid = section([
        article_card(
            "Guia técnico", "12 mar 2026",
            "Como escolher a ensacadeira certa para a sua fábrica de ração",
            "Capacidade, tipo de saco, precisão e integração com a linha de "
            "extrusão: os 5 critérios que decidem o investimento.",
            "https://images.unsplash.com/photo-1543393470-b2f8d68a91f7?w=800&q=80",
            "Comparativo de ensacadeiras para fábrica de ração"),
        article_card(
            "Comparativo", "28 fev 2026",
            "Ensacadeira big bag vs saco de 50 kg: qual é mais eficiente para soja?",
            "Análise de custo, produtividade e logística para produtores de "
            "soja decidirem entre big bag e saco convencional.",
            "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=800&q=80",
            "Big bag de soja vs saco de 50 kg"),
        article_card(
            "Manutenção", "14 fev 2026",
            "Manutenção preventiva de ensacadeiras: o guia completo para indústrias",
            "Calendário de manutenção, peças críticas, indicadores de "
            "disponibilidade e checklist para o operador.",
            "https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800&q=80",
            "Técnico em manutenção preventiva de ensacadeira"),
    ], {**bg_light(), "padding": px(80, 20, 80, 20), "structure": "33"})

    news = section([
        column(100, [
            eyebrow("NEWSLETTER", align="center"),
            amber_divider(align="center"),
            heading("Receba nossos artigos técnicos no e-mail",
                    tag="h2", color="#FFFFFF", fsize=30, align="center", margin_b=16),
            text("Um e-mail por mês com guias práticos para gestores e "
                 "engenheiros de produção.", color="#A8B8C2", fsize=16,
                 align="center", margin_b=32),
            widget("form", {
                "form_name": "Newsletter",
                "form_fields": [
                    {"_id": uid(), "field_type": "email", "field_label": "E-mail",
                     "placeholder": "seu@email.com.br", "width": "100",
                     "required": "true"},
                ],
                "button_text": "Quero receber",
                "button_align": "center", "button_size": "md",
                "button_background_color": "#F0A500",
                "button_text_color": "#0D2137",
                "button_typography_typography": "custom",
                "button_typography_font_family": "Inter",
                "button_typography_font_weight": "700",
            }),
        ]),
    ], {**bg_dark(), "padding": px(80, 20, 80, 20)})
    write_doc(
        slug="blog", title="Blog",
        doc_type="page", template_type="single-page",
        content=[hero, grid, news],
        page_settings={"hide_title": "yes"},
    )

# ============================================================
# contato
# ============================================================
def build_contato():
    hero = hero_dark("Solicite um orçamento personalizado",
                     "Conte sobre seu produto, cadência desejada e tipo de saco. "
                     "Nosso time comercial responde em até 24h úteis.")
    form_widget = widget("form", {
        "form_name": "Solicitação de Orçamento",
        "form_fields": [
            {"_id": uid(), "field_type": "text", "field_label": "Nome completo",
             "placeholder": "Como podemos te chamar?", "width": "100",
             "required": "true"},
            {"_id": uid(), "field_type": "email",
             "field_label": "E-mail corporativo",
             "placeholder": "voce@empresa.com.br", "width": "100",
             "required": "true"},
            {"_id": uid(), "field_type": "tel", "field_label": "WhatsApp",
             "placeholder": "(11) 90000-0000", "width": "50",
             "required": "true"},
            {"_id": uid(), "field_type": "text", "field_label": "Empresa",
             "placeholder": "Razão social ou fantasia", "width": "50",
             "required": "true"},
            {"_id": uid(), "field_type": "select", "field_label": "Segmento",
             "field_options": "Ração animal\nSoja e grãos\nFertilizantes\nQuímica e mineração\nOutro",
             "width": "100", "required": "true"},
            {"_id": uid(), "field_type": "select",
             "field_label": "Produto de interesse",
             "field_options": "Ensacadeira de sopro\nEnsacadeira gravimétrica\nEnsacadeira big bag\nRosca transportadora\nNão sei — preciso de orientação",
             "width": "100", "required": "true"},
            {"_id": uid(), "field_type": "textarea",
             "field_label": "Conte sobre seu processo",
             "placeholder": "Produto, cadência (sacos/h), tipo de saco, prazo desejado...",
             "width": "100", "rows": "5"},
        ],
        "button_text": "Solicitar orçamento",
        "button_align": "left", "button_size": "md",
        "button_background_color": "#F0A500",
        "button_text_color": "#0D2137",
        "button_typography_typography": "custom",
        "button_typography_font_family": "Inter",
        "button_typography_font_weight": "700",
        "label_typography_typography": "custom",
        "label_typography_font_family": "Inter",
        "label_typography_font_weight": "600",
        "label_color": "#0D2137",
    })
    contact_info = column(40, [
        eyebrow("OUTROS CANAIS"),
        amber_divider(),
        heading("Fale conosco direto", tag="h3", fsize=22, margin_b=20),
        widget("icon-list", {
            "view": "traditional",
            "icon_list": [
                {"_id": uid(),
                 "text": "<strong>Comercial</strong><br>(11) 4000-0000",
                 "selected_icon": {"value": "fas fa-phone", "library": "fa-solid"},
                 "link": {"url": "tel:+551140000000"}},
                {"_id": uid(),
                 "text": "<strong>E-mail</strong><br>comercial@automatizaworld.com.br",
                 "selected_icon": {"value": "fas fa-envelope", "library": "fa-solid"},
                 "link": {"url": "mailto:comercial@automatizaworld.com.br"}},
                {"_id": uid(),
                 "text": "<strong>WhatsApp comercial</strong><br>(11) 90000-0000",
                 "selected_icon": {"value": "fab fa-whatsapp", "library": "fa-brands"},
                 "link": {"url": "https://wa.me/5511900000000"}},
                {"_id": uid(),
                 "text": "<strong>Endereço</strong><br>Av. Industrial, 1234 — São Paulo / SP",
                 "selected_icon": {"value": "fas fa-location-dot", "library": "fa-solid"},
                 "link": {"url": ""}},
            ],
            "icon_color": "#F0A500",
            "text_color": "#0D2137",
            "icon_size": size(20),
            "text_typography_typography": "custom",
            "text_typography_font_family": "Inter",
            "text_typography_font_size": size(15),
            "text_typography_line_height": size(1.5, "em"),
            "space_between": size(20),
        }),
        spacer(20),
        text("<strong>Financiamento BNDES disponível.</strong><br>"
             "Consulte condições para sua empresa.",
             color="#5A7A8A", fsize=14, margin_b=0),
    ], {
        "background_background": "classic",
        "background_color": "#F4F6F9",
        "padding": px(40, 40, 40, 40),
        "border_radius": px(8, 8, 8, 8, True),
        "margin": px(0, 0, 0, 30),
    })
    grid = section([
        column(60, [form_widget], {"padding": px(0, 30, 0, 0)}),
        contact_info,
    ], {**bg_white(), "padding": px(80, 20, 80, 20), "structure": "6040"})
    write_doc(
        slug="contato", title="Contato",
        doc_type="page", template_type="single-page",
        content=[hero, grid],
        page_settings={"hide_title": "yes"},
    )

# ============================================================
# 404
# ============================================================
def build_404():
    sec = section([
        column(100, [
            heading("404", tag="h1", color="#F0A500", fsize=120,
                    align="center", weight="700", margin_b=8),
            heading("Página não encontrada", tag="h2", fsize=32,
                    align="center", margin_b=16),
            text("A página que você procura pode ter sido movida, "
                 "renomeada ou nunca existiu. Use o menu acima ou volte "
                 "para a home.", fsize=16, align="center", margin_b=32),
            widget("button", {
                "text": "Voltar para a home",
                "link": {"url": "/", "is_external": ""},
                "align": "center", "size": "md",
                "background_color": "#F0A500",
                "button_text_color": "#0D2137",
                "border_radius": px(4, 4, 4, 4, True),
                "text_padding": px(16, 32, 16, 32),
                "typography_typography": "custom",
                "typography_font_family": "Inter",
                "typography_font_size": size(15),
                "typography_font_weight": "700",
            }),
        ]),
    ], {**bg_light(), "padding": px(140, 20, 140, 20)})
    write_doc(
        slug="404-page", title="404 Page",
        doc_type="error-404", template_type="single-404",
        content=[sec], page_settings=None,
        extra_metadata={
            "elementor_library_type": "error-404",
            "elementor_pro_conditions": ["include/singular/not_found404"],
        },
        extra_info=[
            "This is a \"Error 404\" template for Elementor Pro.",
            "This template will display on: 404 Page.",
        ],
    )

# ============================================================
# manifest.json (Envato Template Kit format: templates = ARRAY)
# ============================================================
def build_manifest():
    PREVIEW = "https://automatizaworld.com.br"

    def entry(name, slug, t_type, category, template_type, info,
              elementor_library_type=None,
              elementor_pro_conditions=None):
        md = {
            "template_type": template_type,
            "include_in_zip": "1",
            "elementor_pro_required": "1",
        }
        if elementor_library_type:
            md["elementor_library_type"] = elementor_library_type
        if elementor_pro_conditions:
            md["elementor_pro_conditions"] = elementor_pro_conditions
        md["additional_template_information"] = info
        return {
            "name": name,
            "screenshot": f"screenshots/{slug}.jpg",
            "source": f"templates/{slug}.json",
            "preview_url": f"{PREVIEW}/{slug}",
            "type": t_type,
            "category": category,
            "metadata": md,
            "elementor_pro_required": True,
        }

    templates = [
        entry("Global Kit Styles", "global", "section", "page",
              "global-styles",
              ["These are the global theme styles configured through the "
               "Elementor Theme Styles area."]),
        entry("Header", "header", "header", "section", "section-header",
              ["This is a \"Header\" template for Elementor Pro.",
               "This template will display on: Entire Site."],
              elementor_library_type="header",
              elementor_pro_conditions=["include/general"]),
        entry("Footer", "footer", "footer", "section", "section-footer",
              ["This is a \"Footer\" template for Elementor Pro.",
               "This template will display on: Entire Site."],
              elementor_library_type="footer",
              elementor_pro_conditions=["include/general"]),
        entry("Home", "home", "section", "page", "single-home",
              ["This is a \"Home\" template for Elementor Pro.",
               "This template will display on: Front Page."]),
        entry("Sobre", "sobre", "page", "page", "single-page",
              ["Página institucional Sobre."]),
        entry("Ensacadeiras", "ensacadeiras", "page", "page", "single-page",
              ["Página de categoria de produtos — Ensacadeiras."]),
        entry("Segmentos", "segmentos", "page", "page", "single-page",
              ["Página de segmentos industriais atendidos."]),
        entry("Serviços", "servicos", "page", "page", "single-page",
              ["Página de serviços de pós-venda."]),
        entry("Blog", "blog", "page", "page", "single-page",
              ["Página de listagem de artigos do blog."]),
        entry("Contato", "contato", "page", "page", "single-page",
              ["Página de contato com formulário de orçamento."]),
        entry("404 Page", "404-page", "error-404", "page", "single-404",
              ["This is a \"Error 404\" template for Elementor Pro.",
               "This template will display on: 404 Page."],
              elementor_library_type="error-404",
              elementor_pro_conditions=["include/singular/not_found404"]),
    ]

    manifest = {
        "manifest_version": "1.0.21",
        "title": "Automatiza World — Ensacadeiras Industriais Elementor Template Kit",
        "page_builder": "elementor",
        "kit_version": "1.0.0",
        "templates": templates,
        "required_plugins": [
            {"name": "Elementor Pro", "version": "3.21.0",
             "file": "elementor-pro/elementor-pro.php",
             "author": "Elementor.com"},
            {"name": "Elementor", "version": "3.21.0",
             "file": "elementor/elementor.php",
             "author": "Elementor.com"},
        ],
        "images": [],
    }
    p = KIT / "manifest.json"
    p.write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                 encoding="utf-8")
    json.loads(p.read_text(encoding="utf-8"))

# ============================================================
# help.html
# ============================================================
HELP_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Automatiza World — Template Kit</title>
<style>
body{font-family:Inter,Arial,sans-serif;max-width:780px;margin:40px auto;padding:0 20px;color:#0D2137;line-height:1.65;}
h1{color:#0D2137;border-bottom:3px solid #F0A500;padding-bottom:12px;}
code{background:#F4F6F9;padding:2px 6px;border-radius:3px;font-size:13px;}
</style>
</head>
<body>
<h1>Automatiza World — Elementor Template Kit</h1>
<p><strong>Versão:</strong> 1.0.0 &nbsp;|&nbsp; <strong>Elementor:</strong> 3.21+ e Elementor Pro 3.21+</p>
<h2>Importação</h2>
<ol>
<li>Instale o plugin <strong>Envato Elements — Template Kit Import</strong> (ou use o importador nativo se sua versão do Elementor Pro suportar Template Kits).</li>
<li>Vá em <strong>Elements → Installed Kits → Upload Template Kit</strong>.</li>
<li>Faça upload de <code>automatiza-world-elementor-kit.zip</code>.</li>
<li>Após o upload, instale os templates desejados (clique em cada um e em <em>Insert</em>).</li>
<li>Aplique o <strong>Global Kit Styles</strong> primeiro para carregar a paleta e tipografia.</li>
<li>Configure o <strong>Header</strong> e o <strong>Footer</strong> em <em>Templates → Theme Builder</em> com a condição <em>Entire Site</em>.</li>
<li>Substitua o placeholder <code>{{LOGO_URL}}</code> no Header e Footer pela URL da sua logo.</li>
</ol>
<h2>Paleta global</h2>
<ul>
<li><strong>Primary (Dark):</strong> <code>#0D2137</code></li>
<li><strong>Accent (Amber):</strong> <code>#F0A500</code></li>
<li><strong>Light:</strong> <code>#F4F6F9</code></li>
<li><strong>Navy 2:</strong> <code>#081E2E</code></li>
<li><strong>Text Muted:</strong> <code>#5A7A8A</code></li>
</ul>
</body>
</html>
"""

def build_help():
    (KIT / "help.html").write_text(HELP_HTML, encoding="utf-8")

# ============================================================
# screenshots (minimal valid JPEG placeholders)
# ============================================================
JPEG_BYTES = bytes([
    0xFF,0xD8,0xFF,0xE0,0x00,0x10,0x4A,0x46,0x49,0x46,0x00,0x01,
    0x01,0x00,0x00,0x01,0x00,0x01,0x00,0x00,0xFF,0xDB,0x00,0x43,
    0x00,0x08,0x06,0x06,0x07,0x06,0x05,0x08,0x07,0x07,0x07,0x09,
    0x09,0x08,0x0A,0x0C,0x14,0x0D,0x0C,0x0B,0x0B,0x0C,0x19,0x12,
    0x13,0x0F,0x14,0x1D,0x1A,0x1F,0x1E,0x1D,0x1A,0x1C,0x1C,0x20,
    0x24,0x2E,0x27,0x20,0x22,0x2C,0x23,0x1C,0x1C,0x28,0x37,0x29,
    0x2C,0x30,0x31,0x34,0x34,0x34,0x1F,0x27,0x39,0x3D,0x38,0x32,
    0x3C,0x2E,0x33,0x34,0x32,0xFF,0xC0,0x00,0x0B,0x08,0x00,0x01,
    0x00,0x01,0x01,0x01,0x11,0x00,0xFF,0xC4,0x00,0x1F,0x00,0x00,
    0x01,0x05,0x01,0x01,0x01,0x01,0x01,0x01,0x00,0x00,0x00,0x00,
    0x00,0x00,0x00,0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,
    0x09,0x0A,0x0B,0xFF,0xC4,0x00,0xB5,0x10,0x00,0x02,0x01,0x03,
    0x03,0x02,0x04,0x03,0x05,0x05,0x04,0x04,0x00,0x00,0x01,0x7D,
    0x01,0x02,0x03,0x00,0x04,0x11,0x05,0x12,0x21,0x31,0x41,0x06,
    0x13,0x51,0x61,0x07,0x22,0x71,0x14,0x32,0x81,0x91,0xA1,0x08,
    0x23,0x42,0xB1,0xC1,0x15,0x52,0xD1,0xF0,0x24,0x33,0x62,0x72,
    0x82,0x09,0x0A,0x16,0x17,0x18,0x19,0x1A,0x25,0x26,0x27,0x28,
    0x29,0x2A,0x34,0x35,0x36,0x37,0x38,0x39,0x3A,0x43,0x44,0x45,
    0x46,0x47,0x48,0x49,0x4A,0x53,0x54,0x55,0x56,0x57,0x58,0x59,
    0x5A,0x63,0x64,0x65,0x66,0x67,0x68,0x69,0x6A,0x73,0x74,0x75,
    0x76,0x77,0x78,0x79,0x7A,0x83,0x84,0x85,0x86,0x87,0x88,0x89,
    0x8A,0x92,0x93,0x94,0x95,0x96,0x97,0x98,0x99,0x9A,0xA2,0xA3,
    0xA4,0xA5,0xA6,0xA7,0xA8,0xA9,0xAA,0xB2,0xB3,0xB4,0xB5,0xB6,
    0xB7,0xB8,0xB9,0xBA,0xC2,0xC3,0xC4,0xC5,0xC6,0xC7,0xC8,0xC9,
    0xCA,0xD2,0xD3,0xD4,0xD5,0xD6,0xD7,0xD8,0xD9,0xDA,0xE1,0xE2,
    0xE3,0xE4,0xE5,0xE6,0xE7,0xE8,0xE9,0xEA,0xF1,0xF2,0xF3,0xF4,
    0xF5,0xF6,0xF7,0xF8,0xF9,0xFA,0xFF,0xDA,0x00,0x08,0x01,0x01,
    0x00,0x00,0x3F,0x00,0xFB,0xD0,0xFF,0xD9
])

def build_screenshots(slugs):
    for s in slugs:
        (SHOTS / f"{s}.jpg").write_bytes(JPEG_BYTES)

# ============================================================
# ID-dedup safety pass
# ============================================================
def validate_ids():
    for p in TPL.glob("*.json"):
        data = json.loads(p.read_text(encoding="utf-8"))
        seen = set()
        def fix(node):
            if isinstance(node, dict):
                if ("id" in node and isinstance(node["id"], str)
                        and len(node["id"]) == 8):
                    if node["id"] in seen:
                        new = uid()
                        while new in seen:
                            new = uid()
                        node["id"] = new
                    seen.add(node["id"])
                for v in node.values():
                    fix(v)
            elif isinstance(node, list):
                for v in node:
                    fix(v)
        fix(data)
        p.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

# ============================================================
# main
# ============================================================
def main():
    if KIT.exists():
        shutil.rmtree(KIT)
    TPL.mkdir(parents=True)
    SHOTS.mkdir(parents=True)

    build_global()
    build_header()
    build_footer()
    build_home()
    build_sobre()
    build_ensacadeiras()
    build_segmentos()
    build_servicos()
    build_blog()
    build_contato()
    build_404()
    build_manifest()
    build_help()

    slugs = ["global", "header", "footer", "home", "sobre", "ensacadeiras",
             "segmentos", "servicos", "blog", "contato", "404-page"]
    build_screenshots(slugs)
    validate_ids()

    # Sanity checks against manifest
    manifest = json.loads((KIT / "manifest.json").read_text())
    for entry in manifest["templates"]:
        src = KIT / entry["source"]
        shot = KIT / entry["screenshot"]
        assert src.exists(), f"missing {src}"
        assert shot.exists(), f"missing {shot}"
    assert (KIT / "help.html").exists()

    # Build ZIP — entries at the ZIP root, no wrapping folder
    zip_path = ROOT / "automatiza-world-elementor-kit.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(KIT.rglob("*")):
            if path.is_file():
                arc = path.relative_to(KIT)
                zf.write(path, arc)
    print(f"Kit built: {zip_path}")
    print(f"Size: {zip_path.stat().st_size:,} bytes")

if __name__ == "__main__":
    main()
