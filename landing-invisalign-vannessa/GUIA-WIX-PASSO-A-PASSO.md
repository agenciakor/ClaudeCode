# Guia passo a passo: colocar a landing page no Wix (para quem nunca usou o editor)

Este guia complementa o `LEIA-ME.md`. Ele parte do ponto em que a página `/invisalign` já foi
criada no editor e explica **onde fica cada botão**. Os nomes podem variar um pouco conforme a
versão do editor, mas a lógica é a mesma. Fontes oficiais no fim do arquivo.

---

## Etapa 0 · Entrar no editor

1. Acesse **wix.com** e entre na conta da clínica.
2. No painel, clique em **Editar site** (ou **Editor**). O editor abre em uma nova aba.
3. Repare na barra **superior**: à direita ficam **Salvar**, **Visualizar** e **Publicar**. Na
   **esquerda** fica a coluna de ícones: **Páginas**, **Elementos (+)**, **Mídia**, etc.

> Dica: o editor salva rascunhos. Nada vai ao ar até você clicar em **Publicar**.

---

## Etapa 1 · Criar a página e deixá-la escondida (com senha)

1. Na coluna da esquerda, clique em **Páginas** (ícone de folhas).
2. Clique em **+ Adicionar página** > **Página em branco**. Dê o nome **Invisalign**.
3. Com a nova página selecionada na lista, clique nos **três pontinhos (⋯)** ao lado do nome
   > **Configurações**. Uma janela abre com abas:
   - **Informações da página**: em "Qual é o endereço (URL) da página?", deixe `invisalign`.
   - **Layout**: escolha a opção **sem cabeçalho e rodapé** ("Página em branco" / "Sem
     cabeçalho e rodapé"). Assim o menu do site não aparece sobre a landing page.
   - **Permissões**: marque **Titulares de senha** e defina uma senha (ex.: `vannessa2026`).
     Só quem tiver a senha vê a página. **Depois da aprovação, volte aqui e marque "Todos".**
   - **SEO (Google)**: desligue a chave **"Mostrar esta página nos resultados de busca"**.
     Isso impede o Google de indexar a prévia. Não atrapalha o Google Ads.
4. Feche a janela. Ainda em **Páginas**, clique de novo nos **⋯** > **Ocultar do menu**.
   A página continua acessível pelo link `clinicaateliedental.com/invisalign`, mas não aparece
   no menu do site.

---

## Etapa 2 · Subir as imagens e copiar as URLs

1. Na coluna da esquerda, clique em **Mídia** (ícone de imagem).
2. Clique em **Fazer upload de mídia** (ou o botão **Upload**). Selecione os **17 arquivos** da
   pasta `imagens/` de uma vez e aguarde terminar.
3. Para copiar a URL de cada arquivo:
   - Ainda em **Mídia**, em **Arquivos do site**, clique em **Mostrar mais** para abrir o
     Gerenciador de Mídia completo.
   - Clique **uma vez** no arquivo para selecioná-lo.
   - Clique no ícone **⋯ (Mais ações)** que aparece sobre o arquivo (ou clique com o botão
     direito) > **Copiar URL**.
   - A URL copiada começa com `https://static.wixstatic.com/media/...`.
4. Cole cada URL em um bloco de notas ao lado do nome do arquivo. Exemplo:

   ```
   logo-atelie-dental-horizontal.png = https://static.wixstatic.com/media/e82d37_xxxxxxxx~mv2.png
   dra-vannessa-hero.jpg             = https://static.wixstatic.com/media/e82d37_yyyyyyyy~mv2.jpg
   ...
   ```

> **Atalho:** se preferir, me envie essa lista com os 17 nomes e URLs. Eu coloco tudo no
> `index.html` e devolvo o arquivo pronto para colar. Aí você pula a Etapa 3.

---

## Etapa 3 · Colocar as URLs no `index.html`

1. Abra o `index.html` em um editor de texto simples (Bloco de Notas no Windows, TextEdit no
   Mac em modo texto puro, ou o VS Code). **Não use o Word.**
2. Logo no começo do arquivo há o bloco `window.LP_CONFIG = { ... }`. Cada campo tem um
   comentário explicando o que é. Troque os caminhos `imagens/...` pelas URLs do Wix, mantendo
   as aspas. Exemplo:

   ```js
   heroDra: 'imagens/dra-vannessa-hero.jpg',
   ```
   vira
   ```js
   heroDra: 'https://static.wixstatic.com/media/e82d37_yyyyyyyy~mv2.jpg',
   ```

3. Campos a preencher: `logo`, `logoRodape`, `heroDra`, `sobreDra` e os 8 caminhos dentro de
   `antesDepois` (4 casos × antes/depois). Os demais (`atendimento`, `clinica`,
   `seloInvisalign`, `produtoInvisalign`) ficam vazios até chegarem as fotos.
4. Salve o arquivo.

---

## Etapa 4 · Colar o código na página

1. No editor, abra a página **Invisalign** (coluna **Páginas** > clique no nome).
2. Na coluna da esquerda, clique em **Elementos (+)** > role até **Incorporar código** >
   **Incorporações populares** > **HTML incorporado** (também chamado de **Incorporar HTML**
   ou **Elemento HTML**). Um quadro cinza aparece na página.
3. Com o quadro selecionado, clique em **Inserir código** (botão que aparece sobre ele).
4. Na janela, escolha **Código** (não "Endereço do site").
5. Abra o `index.html` no editor de texto, selecione **tudo** (Ctrl+A / Cmd+A), copie
   (Ctrl+C) e cole na caixa (Ctrl+V). Clique em **Atualizar** / **Aplicar**.
6. Feche a janela. O quadro passa a mostrar a página.

---

## Etapa 5 · Ajustar posição, largura e altura

O elemento HTML tem **tamanho fixo**: ele não cresce sozinho com o conteúdo.

1. **Posição:** arraste o quadro para o topo da página (ou, com ele selecionado, use a barra de
   ferramentas flutuante > ícone de **Posição/Tamanho** e coloque **X = 0, Y = 0**).
2. **Largura:** com o quadro selecionado, clique no ícone **Esticar** (duas setas para os lados,
   na barra de ferramentas que aparece ao lado do elemento) e ative **Esticar para a largura
   total** com margens 0.
3. **Altura no desktop:**
   - No `index.html`, dentro do `LP_CONFIG`, mude `mostrarAltura: false` para
     `mostrarAltura: true` e cole o código de novo (Etapa 4, passos 3 a 5).
   - Clique em **Visualizar** (topo, à direita). No canto superior esquerdo da página aparece uma
     etiqueta vermelha: **"altura necessária: 13.0xx px"**.
   - Volte ao editor, selecione o quadro, abra **Posição/Tamanho** e coloque em **Altura (H)**
     esse valor + 20. Como referência: cerca de **13.050 px** no desktop de 1280 px.
   - Se não conseguir digitar a altura, arraste a alça inferior do quadro até ele terminar logo
     abaixo do rodapé marrom escuro da landing page.
4. **Altura no celular:**
   - No topo do editor há um ícone de **celular** (alternar para o editor mobile). Clique nele.
   - Selecione o quadro. Ele já vem esticado. Ajuste a **altura** do mesmo jeito: referência de
     **17.400 px** para a largura mobile de 320 px (a etiqueta vermelha também aparece no
     Visualizar do mobile).
5. Volte `mostrarAltura` para `false` e cole o código de novo. Isso tira a etiqueta vermelha.
6. Sempre que trocar fotos ou textos, meça a altura de novo, porque ela muda.

---

## Etapa 6 · Botão flutuante do WhatsApp que acompanha a rolagem

O botão fica no arquivo `wix-codigo-personalizado.html`, junto com o rastreamento. Ele é criado na
própria página do site, por isso segue a tela no desktop e no celular, com o texto "Estamos online ·
Agende sua avaliação".

1. No painel do Wix (fora do editor): **Configurações** > **Código personalizado** > **+ Adicionar código**.
2. Cole o conteúdo inteiro de `wix-codigo-personalizado.html`.
3. Nome: `LP Invisalign – botão e conversões`. Em **Adicionar código a**, escolha **Páginas escolhidas**
   e marque só a página da landing page. Em **Posicionar código em**, escolha **Head**. Salve.
4. O código personalizado só roda no site **publicado**: publique e abra a página para conferir.

Se o site tiver o aplicativo **Smartarget WhatsApp** (ou outro botão de WhatsApp de app), remova-o
ou desative-o nesta página, para não ficarem dois botões: painel > **Apps** > Smartarget > gerenciar/
remover. Esse app também mostra um aviso "Smartarget Apps are hidden" no plano gratuito.

---

## Etapa 7 · Publicar a prévia

1. Clique em **Publicar** (canto superior direito) > **Publicar**.
2. Abra `https://www.clinicaateliedental.com/invisalign` em uma janela anônima. O Wix pede a
   senha da Etapa 1. Depois de digitar, a landing page aparece.
3. Envie o link e a senha para quem vai aprovar.

**Depois da aprovação:** Páginas > ⋯ > Configurações > **Permissões** > **Todos**, e
**Publicar** de novo. Só então ative a campanha do Google Ads (veja rastreamento no `LEIA-ME.md`).

---

## Problemas comuns

| O que aparece | Causa provável | Solução |
|---|---|---|
| Quadro em branco depois de colar | Colou no modo "Endereço do site" | Repita a Etapa 4 e escolha **Código** |
| Fotos aparecem como espaço bege com legenda | URL errada ou não trocada | Confira no `LP_CONFIG` se cada campo tem a URL do Wix entre aspas |
| A página corta no meio | Altura do elemento menor que a necessária | Etapa 5 |
| Faixa escura vazia abaixo do rodapé | Altura maior que a necessária | Reduza a altura, ou deixe: a faixa é da cor do rodapé de propósito |
| Botão do WhatsApp abre dentro do quadro | O Wix bloqueou nova aba | Confira se o link do botão do Wix está com "nova aba" |

---

## Fontes (documentação oficial do Wix)

- Incorporar código HTML: https://support.wix.com/pt/article/incorporar-c%C3%B3digo-personalizado-ao-site
- Copiar a URL de um arquivo do Gerenciador de Mídia: https://support.wix.com/pt/article/wix-media-recuperar-o-url-de-um-arquivo-no-gerenciador-de-m%C3%ADdia
- Sobre incorporações e códigos: https://support.wix.com/pt/article/adicionando-c%C3%B3digo-ao-seu-site
- HTML no editor mobile: https://support.wix.com/pt/article/c%C3%B3digo-html-no-mobile
