# Home · Clínica Ateliê Dental (clinicaateliedental.com)

Nova página inicial no mesmo padrão visual da landing page do Invisalign: paleta de marrons da marca
com o verde de contraste, fontes Fahkwang e Montserrat, cards, botões e espaçamentos iguais.

| Arquivo | Para que serve |
|---|---|
| `index.html` | A Home completa (sem menu). É **este arquivo inteiro** que vai no Elemento HTML da página inicial. |
| `CABECALHO-WIX.md` | Como montar o menu e o cabeçalho nativo do Wix, com cores, fontes e links. |
| `imagens/` | Fotos da clínica (recortadas e otimizadas), equipe, logos e Invisalign. |
| `URLS-PARA-PREENCHER.txt` | Lista dos arquivos que precisam subir no Wix, para colar as URLs. |
| `preview/` | Prévia com imagens embutidas e prints, para aprovação. |

## Seções da Home (de cima para baixo)

1. **Hero**: "Promovemos sorrisos e autoestima", foto da recepção, botões WhatsApp e Invisalign, selos.
2. **Faixa de credenciais**: nota 5,0 (101 avaliações), dois especialistas, Invisalign Platinum Elite, endereço.
3. **Especialidades**: 11 cards. Só o de **Alinhador invisível (Invisalign®)** tem link, para a landing. Os outros ganham link quando as páginas existirem (basta transformar o `<div class="esp">` em `<a class="esp" href="...">`).
4. **Invisalign em destaque**: alinhador em 3D, troféu Top Doctor 2026 e botões para a landing.
5. **A clínica**: texto, três pilares e galeria com 6 fotos.
6. **Equipe**: Dra. Vannessa Borsato e Dr. Delson Borsato, com currículo e CRO.
7. **Ateliê Facial**: bloco escuro "Conheça também", com botão para a página `/atelie-facial` (a criar).
8. **Depoimentos**: carrossel com as avaliações do Google (3 por vez, loop infinito) e links para Google e Instagram.
9. **Contato**: endereço, horário, telefone/WhatsApp, e-mail, redes e mapa.
10. **Chamada final** e **rodapé** com CRO da clínica, CNPJ, responsáveis técnicos e política de privacidade.

Tudo o que é editável fica no bloco `SITE_CONFIG`, no começo do `index.html` (fotos, links, depoimentos, nota).

## Como publicar

1. **Imagens:** suba os arquivos listados em `URLS-PARA-PREENCHER.txt` no Gerenciador de Mídia e me mande as URLs (ou cole no `SITE_CONFIG`). Dra. Vannessa, logo e Invisalign já estão no Wix e já estão preenchidos.
2. **Cabeçalho e menu:** siga o `CABECALHO-WIX.md`.
3. **Página inicial:** no editor, abra a página *Início*, apague as seções atuais (carrossel de banners, "Conheça quem faz acontecer", especialidades, "Seu sorriso...", "Pessoas reais", depoimentos e o formulário de contato), deixando **só o cabeçalho e o rodapé do Wix**. Se preferir, apague o rodapé do Wix também: a Home já tem rodapé próprio com os dados obrigatórios do CFO.
4. *Adicionar > Incorporar código > HTML incorporado > Código*, cole o `index.html`, estique para a largura total e ajuste a altura (referências abaixo). O mesmo procedimento da landing, inclusive o `mostrarAltura: true` para medir.
5. **Código personalizado:** o botão flutuante do WhatsApp e o rastreamento já estão no `wix-codigo-personalizado.html` da landing. Em *Configurações > Código personalizado*, edite aquele código e, em "Adicionar código a", marque também a página **Início** (ou "Todas as páginas"). Nada mais muda.
6. **Smartarget:** remova o app, para não ficar um segundo botão de WhatsApp na Home.
7. Publique e confira no celular.

Alturas de referência (sem o cabeçalho do Wix):

| Largura do elemento | Altura |
|---|---|
| 280 px (mobile clássico) | ≈ 16.200 px |
| 320 px (mobile clássico) | ≈ 15.000 px |
| 390 px | ≈ 13.900 px |
| 768 px | ≈ 12.400 px |
| 980 px | ≈ 9.950 px |
| 1280 px | ≈ 9.750 px |
| 1440 px ou mais | ≈ 9.860 px |

## Pendências

- [ ] Subir as fotos da clínica, do Dr. Delson e a logo da Ateliê Facial no Wix e colar as URLs
- [ ] Montar o cabeçalho e o menu (CABECALHO-WIX.md)
- [ ] Criar a página `/atelie-facial` (o botão "Conhecer a Ateliê Facial" aponta para ela)
- [ ] Criar as páginas das demais especialidades, uma a uma, e ligar os cards
- [ ] Confirmar com o Dr. Delson a redação do currículo (copiada do site atual)
- [ ] Autorização de uso de imagem dos pacientes, caso as fotos "Pessoas reais" do site antigo voltem a ser usadas (não estão na nova Home)
