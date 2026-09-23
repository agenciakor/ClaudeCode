# Landing page Invisalign · Dra. Vannessa Borsato · Clínica Ateliê Dental

Página de alta conversão para a campanha de Google Ads de alinhadores invisíveis (Invisalign®).
Feita para ser colada no Wix como **Elemento HTML**.

| Arquivo | Para que serve |
|---|---|
| `index.html` | A landing page completa. É **este arquivo inteiro** que vai dentro do Elemento HTML do Wix. |
| `wix-codigo-personalizado.html` | Código de rastreamento das conversões (cliques no WhatsApp), que vai em *Configurações > Código personalizado* do Wix. |
| `LEIA-ME.md` | Este guia. |

---

## 1. Antes de publicar: preencher o bloco `LP_CONFIG`

Tudo o que é editável fica no começo do `index.html`, no bloco `window.LP_CONFIG = { ... }`.
Não é preciso mexer em mais nada.

### Fotos (pendente: o Drive não pôde ser acessado daqui)
1. No Wix, abra o **Gerenciador de Mídia** e suba as fotos.
2. Clique na foto > **Copiar URL** (a URL começa com `https://static.wixstatic.com/media/...`).
3. Cole a URL entre as aspas do campo certo:

| Campo | Foto ideal |
|---|---|
| `logo` | Logo em PNG/SVG com fundo transparente, versão para fundo claro |
| `logoRodape` | Logo em versão clara (branca ou bege) para o rodapé verde-escuro (opcional) |
| `heroDra` | **Foto principal**: Dra. sorrindo, vertical (4:5), cerca de 1000×1250 px, fundo limpo |
| `atendimento` | Dra. atendendo ou mostrando o alinhador, horizontal (3:2) |
| `sobreDra` | Retrato profissional, vertical (4:5) |
| `clinica` | 3 fotos da clínica, horizontais (3:2): recepção, consultório, detalhes |

Enquanto um campo estiver vazio, a página mostra um espaço reservado elegante com a legenda da foto que falta.

### Antes e depois (pendente)
Cada caso é uma linha com foto de antes, foto de depois, nome e descrição:
```js
antesDepois: [
  { antes: 'URL_ANTES', depois: 'URL_DEPOIS', paciente: 'Maria S.', descricao: 'Dentes apinhados · 12 meses' },
],
```
- A seção **só aparece** quando existe pelo menos 1 caso preenchido.
- O visitante arrasta a linha sobre a foto para comparar.
- Tire as duas fotos com **o mesmo enquadramento e a mesma luz**, sem filtro nem edição.
- **Obrigatório:** autorização por escrito do paciente (Res. CFO-196/2019). As fotos devem mostrar o diagnóstico (antes) e o resultado final (depois).

### Depoimentos (pendente)
```js
depoimentos: [
  { nome: 'Nome do paciente', texto: 'Texto copiado da avaliação real no Google', origem: 'Google', foto: '' },
],
notaGoogle: '5,0',
totalAvaliacoesGoogle: '87',
```
- A seção **só aparece** com pelo menos 1 depoimento. Use somente avaliações reais.
- A nota e o total só aparecem se preenchidos.

### Outros campos
- `textoAvaliacao`: texto sobre a consulta de avaliação, que aparece na pergunta "Como funciona a consulta de avaliação?" (pendente, aguardando a Dra.). **Não coloque valor.**
- `links.privacidade`: URL da política de privacidade do site (recomendado para o Google Ads).
- `responsavelTecnico`: **confirme** quem é o responsável técnico da clínica. Hoje está preenchido com a Dra. Vannessa.
- `mostrarAltura`: ajuda para acertar a altura no Wix (veja a seção 2).

---

## 2. Como colocar no Wix

1. **Crie uma página nova** (ex.: `/invisalign`).
2. Em *Configurações da página > Layout*, deixe a página **sem cabeçalho e sem rodapé do site**. A landing page já tem topo e rodapé próprios, e tirar o menu evita fugas do funil.
3. *Adicionar (+) > Incorporar código > **Incorporar HTML***. Escolha **Código** e cole **todo** o conteúdo do `index.html`. Clique em *Atualizar*.
4. Estique o elemento para a **largura total** da página e alinhe-o ao topo (posição 0).
5. **Altura**: o Elemento HTML do Wix tem altura fixa, que não se ajusta sozinha ao conteúdo.
   - No `LP_CONFIG`, mude `mostrarAltura` para `true` e clique em *Atualizar*.
   - Abra o **Visualizar**. Uma etiqueta vermelha no topo mostra a altura necessária.
   - Defina a altura do elemento com esse valor + 20 px. Faça isso no **desktop** e depois no **editor mobile**, onde a altura é diferente.
   - Volte `mostrarAltura` para `false` e atualize.
   - **Sempre que adicionar fotos, casos ou depoimentos, meça de novo**, porque a altura muda.
   - Tabela de referência (sem as seções opcionais, com as fotos principais):

   ALTURAS_TABELA

6. **SEO da página** (*Configurações da página > SEO*):
   - Título: `Invisalign em Curitiba | Dra. Vannessa Borsato, Ortodontista`
   - Descrição: `Alinhadores invisíveis Invisalign com especialista em Ortodontia e Invisalign Doctor. Clínica Ateliê Dental, Campina do Siqueira. Agende sua avaliação.`
   - Se não quiser que a página apareça na busca orgânica, marque "não indexar". Isso **não** atrapalha o Google Ads.
7. **Botão flutuante de WhatsApp (recomendado para o celular)**: um botão fixo na tela não funciona dentro do Elemento HTML. Por isso, crie no próprio Wix um botão com o ícone do WhatsApp, marque *Fixar na tela* (canto inferior direito) e aponte para o mesmo link da página:
   `https://wa.me/554130726994?text=Ol%C3%A1%20Tenho%20interesse%20em%20saber%20mais%20sobre%20Invisalign.%20*N%C3%83O%20APAGUE%20ESSA%20MENSAGEM%20VOC%C3%8A%20TEM%20PREFER%C3%8ANCIA*`

---

## 3. Rastreamento de conversões (Google Ads) · pendente dos IDs

A página roda dentro de um iframe do Wix, em outro domínio. Uma tag do Google Ads colocada dentro dela **não** é atribuída ao anúncio. Por isso o esquema funciona assim:

1. Cada clique em um botão do WhatsApp da landing page envia um aviso (`postMessage`) para o site Wix, informando **qual** botão foi clicado: `topo`, `hero`, `beneficios`, `contato` ou `final`.
2. O código de `wix-codigo-personalizado.html`, que vai em *Configurações > Código personalizado > Head*, só na página da landing page, recebe esse aviso e:
   - envia o evento `lp_whatsapp_click` ao **Google Tag Manager**, **ou**
   - dispara a conversão do **Google Ads** direto, se o gtag estiver instalado. Nesse caso, preencha `AW-XXXXXXXXXX/XXXXXXXX`.

**Configuração recomendada (GTM):**
- Conecte o GTM em *Marketing e SEO > Integrações de marketing > Google Tag Manager*.
- No GTM, crie:
  - um acionador *Evento personalizado* com nome `lp_whatsapp_click`;
  - uma tag *Acompanhamento de conversões do Google Ads* usando esse acionador;
  - a tag *Vinculador de conversões* em todas as páginas.
- Teste no modo **Visualizar** do GTM antes de ativar a campanha.
- O clique no botão flutuante nativo do Wix (item 2.7) é rastreado no GTM com um acionador de *Clique em link* cuja URL contém `wa.me`.

---

## 4. Decisões de conformidade (CFO e Google Ads)

- **Preço e condições de pagamento não aparecem na página.** O Código de Ética Odontológica (Res. CFO-118/2012, art. 44) proíbe anunciar preços, serviços gratuitos e modalidades de pagamento. Por isso o valor da avaliação (R$ 200) e o parcelamento em 12x ficam para o atendimento no WhatsApp.
- A página identifica a profissional (nome e CRO-PR 26722), a clínica (CRO-PR 6780 e CNPJ) e o responsável técnico.
- Não há promessa de resultado. O texto deixa claro que a indicação depende de avaliação.
- "Invisalign" e "ClinCheck" aparecem com ® e com a nota de marca registrada da Align Technology. **Não use o logotipo oficial do Invisalign** sem o kit de marca fornecido pela Align ao Invisalign Doctor.
- Antes e depois somente com autorização assinada, sem edição de imagem (Res. CFO-196/2019).

## 5. Pendências

- [ ] Fotos (logo, Dra. e clínica), para subir no Wix e colar as URLs
- [ ] Casos de antes e depois, com autorização dos pacientes
- [ ] Depoimentos reais do Google e nota
- [ ] Detalhes da consulta de avaliação (`textoAvaliacao`)
- [ ] Confirmar o responsável técnico da clínica
- [ ] URL da política de privacidade
- [ ] IDs do Google Ads e do GTM
- [ ] Cores oficiais da marca: a paleta está em variáveis no início do `<style>` (`--brand`, `--accent` etc.) e pode ser trocada em um minuto
