# Home · Clínica Ateliê Dental (clinicaateliedental.com)

Nova página inicial no mesmo padrão visual da landing page do Invisalign: paleta de marrons da marca
com o verde de contraste, fontes Fahkwang e Montserrat, cards, botões e espaçamentos iguais.

| Arquivo | Para que serve |
|---|---|
| `index.html` | A Home completa (sem menu). É **este arquivo inteiro** que vai no Elemento HTML da página inicial. |
| `CABECALHO-WIX.md` | Como montar o menu e o cabeçalho nativo do Wix, com cores, fontes e links. |
| `imagens/` | Fotos da clínica (recortadas e otimizadas), equipe, logos e Invisalign. |
| `../landing-invisalign-vannessa/wix-codigo-personalizado.html` | Código personalizado (botão flutuante + rastreamento), agora válido para o site inteiro. |
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
5. **Código personalizado:** o botão flutuante do WhatsApp e o rastreamento já estão no `wix-codigo-personalizado.html` da landing. Ele foi atualizado para detectar a página: na landing usa a mensagem da campanha, nas outras páginas usa a mensagem geral do site. Em *Configurações > Código personalizado*, cole a versão nova no lugar da atual e deixe "Adicionar código a" em **Todas as páginas**.
6. **SEO da página Início** (*Páginas > Início > Configurações > SEO*). Importante: o Google não lê o conteúdo do Elemento HTML como parte da página, então o título, a descrição e um H1 precisam estar no próprio Wix:
   - Título: `Clínica Ateliê Dental | Dentista e Invisalign em Curitiba`
   - Descrição: `Dentista em Curitiba, na Campina do Siqueira: Invisalign, implantes, facetas, clareamento e cirurgia bucomaxilofacial. Dra. Vannessa Borsato e Dr. Delson Borsato. Agende pelo WhatsApp.`
   - "Mostrar esta página nos resultados de busca": **ligado**.
   - Acima do Elemento HTML, adicione um **texto nativo do Wix** marcado como **H1** com `Clínica odontológica em Curitiba · Ateliê Dental`, em Fahkwang 14 px cor `#8A6136` (fica como uma linha discreta sobre o hero). Opcional, mas recomendado: um texto pequeno abaixo do bloco HTML com o endereço e os tratamentos, para a página ter conteúdo próprio indexável.
7. **Smartarget:** remova o app, para não ficar um segundo botão de WhatsApp na Home.
8. Publique e confira no celular.

Alturas de referência (sem o cabeçalho do Wix):

| Largura do elemento | Altura |
|---|---|
| 280 px (mobile clássico) | ≈ 16.400 px |
| 320 px (mobile clássico) | ≈ 15.400 px |
| 390 px | ≈ 14.100 px |
| 768 px | ≈ 12.400 px |
| 980 px | ≈ 9.950 px |
| 1280 px | ≈ 9.850 px |
| 1440 px ou mais | ≈ 9.950 px |

## Conferência do site publicado (10/10/2026)

A nova Home e o cabeçalho já estão no ar. O que ainda precisa de ajuste, visto no site ao vivo:

- [ ] **Celular:** o Elemento HTML está com **98 px de altura** na versão mobile, então a Home quase não aparece no celular. No editor mobile, selecione o elemento e ajuste a altura (≈ 16.400 px com o elemento a 280 px de largura; ≈ 15.400 px se esticar para 320 px).
- [ ] **Botão flutuante:** o código personalizado está aplicado só à landing. Editar o trecho, colar a versão nova e marcar **Todas as páginas**.
- [ ] **Botão do cabeçalho "Agendar Avaliação":** está com a mensagem da campanha do Invisalign. Trocar pelo link geral do site (está no `CABECALHO-WIX.md`).
- [ ] **Itens "A Clínica" e "Contato" do menu:** apontam para a Home sem âncora. Criar as âncoras `clinica` e `contato` e ligar os itens a elas.
- [ ] **Subitem do menu:** renomear "Alinhador Invisível | Invisalig" para "Alinhador Invisível (Invisalign®)" em *Páginas e menu* (só o nome do item, a URL não muda).
- [ ] **SEO da página Início:** título ainda é "Clínica Odontológica Ateliê Dental | Ateliê Facial" e não há H1. Seguir o passo 6 acima.
- [x] App "Google Reviews" (selo "5.0 · 10 reviews" no canto inferior esquerdo) removido pelo cliente.

## Pendências

- [x] Subir as fotos da clínica, do Dr. Delson e a logo da Ateliê Facial no Wix e colar as URLs (feito: todas as imagens já vêm do Wix)
- [ ] Montar o cabeçalho e o menu (CABECALHO-WIX.md)
- [ ] Criar a página `/atelie-facial` (o botão "Conhecer a Ateliê Facial" aponta para ela)
- [ ] Criar as páginas das demais especialidades, uma a uma, e ligar os cards
- [ ] Confirmar se a especialidade em Cirurgia e Traumatologia Bucomaxilofacial do Dr. Delson está **registrada no CRO-PR**. Só com o registro a página pode chamá-lo de "especialista" (hoje diz "residência em CTBMF", que é o que foi informado)
- [ ] Decidir se os cursos de aperfeiçoamento e imersão continuam no card do Dr. Delson (o CFO só prevê, em publicidade, especialidades registradas e títulos stricto sensu; estão lá porque constam no site atual)
- [ ] Autorização de uso de imagem dos pacientes, caso as fotos "Pessoas reais" do site antigo voltem a ser usadas (não estão na nova Home)
