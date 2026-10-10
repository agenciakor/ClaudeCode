# Cabeçalho e menu do site no Wix (Opção A: cabeçalho nativo)

O menu fica no **cabeçalho do próprio Wix**, fora do bloco HTML. Assim ele fixa no topo ao rolar,
vira "hambúrguer" no celular sozinho e aparece em todas as páginas. Vocês acrescentam as próximas
especialidades no menu sem mexer em código.

## 1. Estrutura do menu

| Item | Tipo | Destino |
|---|---|---|
| **Início** | link | página inicial (`/`) |
| **A Clínica** | link | página inicial, seção "A clínica" (âncora `#clinica`, veja o passo 4) |
| **Especialidades** | pasta/dropdown | sem destino próprio; abre o submenu |
| ↳ Alinhador Invisível (Invisalign®) | subitem | `/alinhador-invisivel-invisalig` |
| **Contato** | link | página inicial, seção "Contato" (âncora `#contato`) |
| **Agendar avaliação** (botão) | botão | link do WhatsApp (abaixo) |

Link do WhatsApp do botão:
`https://wa.me/554130726994?text=Ol%C3%A1%2C%20conheci%20o%20site%20e%20quero%20agendar%20um%20atendimento.%20Ref.%20WUAF9XQ`

Novas especialidades: *Páginas > Especialidades (pasta) > + Adicionar subpágina*. Cada página nova
já entra no dropdown automaticamente.

Páginas que **não** entram no menu: `politica-de-privacidade` (link só no rodapé) e, por enquanto,
`atelie-facial` (quando a página existir, entra como item próprio "Ateliê Facial").

## 2. Visual do cabeçalho (igual à landing page)

| Elemento | Valor |
|---|---|
| Fundo | `#FFF8F1` (creme), linha inferior `#E3DBD0` de 1 px |
| Altura | 76 px no desktop, 64 px no celular |
| Logo | `logo-atelie-dental-horizontal.png` (a mesma da landing), altura 44 px, alinhada à esquerda, link para a página inicial |
| Itens do menu | fonte **Montserrat** 600, 15 px, cor `#231911`; ao passar o mouse `#206B67`; item ativo `#206B67` |
| Dropdown | fundo `#FFFFFF`, borda `#E3DBD0`, cantos 12 px, itens Montserrat 500, 14 px |
| Botão "Agendar avaliação" | fundo `#206B67`, texto branco Montserrat 700, 14 px, cantos 999 px (pílula), altura 44 px; hover `#1A5955` |
| Comportamento | **Fixar** (fica visível ao rolar); no celular, menu hambúrguer com os mesmos itens e o botão do WhatsApp no fim |

## 3. Passo a passo no editor

1. Abra o editor > clique no **cabeçalho** (faixa do topo) > **Configurações do cabeçalho** > em
   *Rolagem*, escolha **Fixo** (ou "Congela" / "Fixar").
2. Fundo: **Mudar design do cabeçalho** > cor `#FFF8F1`, borda inferior 1 px `#E3DBD0`, sem sombra.
3. **Logo:** apague as duas logos atuais (Dental + Facial). Adicione uma imagem com
   `logo-atelie-dental-horizontal.png` (já está no Gerenciador de Mídia), altura 44 px, e ligue ao
   **Início** (*Link > Página > Início*).
4. **Âncoras:** na página inicial, adicione duas âncoras do Wix (*Adicionar > Mais > Âncora*) chamadas
   `clinica` e `contato`, posicionadas sobre o bloco HTML na altura dessas seções. Posições medidas
   a partir do **topo do Elemento HTML** (não do topo da página):

   | Tela | Âncora `clinica` | Âncora `contato` | Altura do HTML |
   |---|---|---|---|
   | Desktop (elemento com 1280 px ou mais) | ≈ 3.720 px (37 %) | ≈ 8.120 px (82 %) | ≈ 9.950 px |
   | Celular (elemento com 320 px) | ≈ 6.730 px (45 %) | ≈ 12.590 px (83 %) | ≈ 15.100 px |

   No editor mobile as âncoras podem ser movidas separadamente; use a segunda linha da tabela.
   Elas servem para os itens *A Clínica* e *Contato* do menu.
5. **Menu:** *Adicionar > Menu > Menu horizontal*. Em **Gerenciar menu**:
   - mantenha só `Início`, `A Clínica` (link: âncora `clinica`), `Especialidades` (pasta) com o
     subitem `Alinhador Invisível (Invisalign®)` (link: página `/alinhador-invisivel-invisalig`),
     e `Contato` (link: âncora `contato`);
   - **Design do menu:** fonte Montserrat 600 15 px, cor `#231911`, hover `#206B67`, sem fundo;
     dropdown com fundo branco, borda `#E3DBD0`, cantos 12 px.
6. **Botão:** *Adicionar > Botão*, texto `Agendar avaliação`, link do WhatsApp acima (abrir em
   nova aba), design: fundo `#206B67`, texto branco Montserrat 700 14 px, cantos 999 px.
7. Organize na linha: logo à esquerda, menu ao centro/direita, botão à direita. Ative
   **Esticar** o cabeçalho e centralize o conteúdo na largura de 1160 px.
8. Clique no ícone de **celular** e confira o menu mobile: logo à esquerda, hambúrguer à direita;
   no menu aberto, os mesmos itens e o botão do WhatsApp por último.

## 4. Fontes no Wix

Se Montserrat não aparecer na lista: *Design do site > Texto > Fontes > Adicionar fontes* e procure
"Montserrat" (fontes do Google já estão disponíveis no Wix). Fahkwang é usada só dentro do HTML.

## 5. Landing page do Invisalign

A landing está configurada como página **sem cabeçalho e rodapé**. Com o novo cabeçalho global,
recomendo manter assim durante a campanha (menos saídas da página = mais conversão). Se preferirem
que o menu apareça lá também: *Páginas > Alinhadores > Configurações > Layout > com cabeçalho*.
