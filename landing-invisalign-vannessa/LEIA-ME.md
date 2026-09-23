# Landing page Invisalign · Dra. Vannessa Borsato · Clínica Ateliê Dental

Página de alta conversão para a campanha de Google Ads de alinhadores invisíveis (Invisalign®).
Feita para ser colada no Wix como **Elemento HTML**.

| Arquivo | Para que serve |
|---|---|
| `index.html` | A landing page completa. É **este arquivo inteiro** que vai dentro do Elemento HTML do Wix. |
| `wix-codigo-personalizado.html` | Código de rastreamento das conversões (cliques no WhatsApp), que vai em *Configurações > Código personalizado* do Wix. |
| `LEIA-ME.md` | Este guia. |
| `preview/` | Prints da página inteira (desktop e celular) para aprovação do layout. |

---

## 1. Antes de publicar: preencher o bloco `LP_CONFIG`

Tudo o que é editável fica no começo do `index.html`, no bloco `window.LP_CONFIG = { ... }`.
Não é preciso mexer em mais nada.

### Fotos
As fotos da Dra. já estão otimizadas na pasta `imagens/` (JPG e WebP, 1000×1250 px, corte 4:5):
- `dra-vannessa-hero.jpg` → campo `heroDra`
- `dra-vannessa-retrato.jpg` → campo `sobreDra`
- `dra-vannessa-quadrado.jpg` → extra, para redes sociais ou imagem de compartilhamento

Hoje o `LP_CONFIG` aponta para `imagens/...` **só para a aprovação do layout**. No Wix isso não funciona:
1. No Wix, abra o **Gerenciador de Mídia** e suba os arquivos da pasta `imagens/`.
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
Cada caso é uma linha com foto de antes, foto de depois e descrição:
```js
antesDepois: [
  { antes: 'URL_ANTES', depois: 'URL_DEPOIS', descricao: 'Dentes apinhados · 12 meses', autorizado: true },
],
```
- A seção **só aparece** quando existe pelo menos 1 caso com `autorizado: true`. Esse campo confirma que o termo de autorização (TCLE) está assinado.
- O visitante arrasta a linha sobre a foto para comparar. A legenda sai automaticamente como "Caso 1 · Dra. Vannessa Borsato, CRO-PR 26722".
- **O nome do paciente não aparece.** O CFO-118/2012, art. 44, VI, proíbe identificar o paciente em publicidade, mesmo com consentimento.
- Use somente casos tratados pela própria Dra. Vannessa, **apenas a foto inicial e a final**, com o mesmo enquadramento e a mesma luz, sem filtro nem edição (Res. CFO-196/2019).
- ⚠️ Os CROs interpretam a Res. 196/2019 como restrita ao profissional, não à clínica (pessoa jurídica). Como a página está no site da clínica, vale confirmar com o CRO-PR antes de ativar esta seção.

### Depoimentos (pendente)
```js
depoimentos: [
  { nome: 'Ana P.', texto: 'Texto copiado da avaliação real no Google', origem: 'Google', estrelas: 5 },
],
notaGoogle: '4,9',
totalAvaliacoesGoogle: '87',
```
- A seção **só aparece** com pelo menos 1 depoimento. Use somente avaliações reais, copiadas sem alteração.
- Nome: primeiro nome + inicial do sobrenome, sem foto do paciente.
- `estrelas` = a nota real daquela avaliação. Sem esse campo, nenhuma estrela é exibida.
- A nota e o total do Google só aparecem se preenchidos.

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
4. Alinhe o elemento ao topo (posição 0) e estique para a largura total.
   - **Editor clássico:** faça a medição do passo 5 com a janela do navegador em **1440 px ou mais**. Em telas menores a página fica um pouco mais curta e sobra uma faixa escura abaixo do rodapé, que se confunde com ele.
   - **Wix Studio:** no Tablet e no Mobile, use largura fixa em px, centralizada (Tablet 740 px, Mobile 320 px), e meça a altura em cada breakpoint.
5. **Altura**: o Elemento HTML do Wix tem altura fixa, que não se ajusta sozinha ao conteúdo.
   - No `LP_CONFIG`, mude `mostrarAltura` para `true` e clique em *Atualizar*.
   - Abra o **Visualizar**. Uma etiqueta vermelha no topo mostra a altura necessária.
   - Defina a altura do elemento com esse valor + 20 px. Faça isso no **desktop** e depois no **editor mobile**, onde a altura é diferente.
   - Volte `mostrarAltura` para `false` e atualize.
   - **Sempre que adicionar fotos, casos ou depoimentos, meça de novo**, porque a altura muda.
   - O FAQ já reserva o espaço da maior resposta, então abrir e fechar perguntas **não** muda a altura da página.
   - Tabela de referência, medida **sem** antes e depois, depoimentos e galeria (esses blocos aumentam a altura):

     | Largura do elemento | Altura |
     |---|---|
     | 280 px (mobile clássico) | ≈ 19.000 px |
     | 320 px (mobile clássico) | ≈ 17.360 px |
     | 390 px | ≈ 15.530 px |
     | 768 px | ≈ 12.850 px |
     | 980 px | ≈ 10.760 px |
     | 1280 px | ≈ 10.960 px |
     | 1440 px ou mais | ≈ 11.200 px |

6. **SEO da página** (*Configurações da página > SEO*):
   - Título: `Invisalign em Curitiba | Dra. Vannessa Borsato, Ortodontista`
   - Descrição: `Alinhadores invisíveis Invisalign com especialista em Ortodontia e Invisalign Doctor. Clínica Ateliê Dental, Campina do Siqueira. Agende sua avaliação.`
   - Se não quiser que a página apareça na busca orgânica, marque "não indexar". Isso **não** atrapalha o Google Ads.
7. **Botão flutuante de WhatsApp**: a página já traz um botão verde redondo (`botaoFlutuante: true` no `LP_CONFIG`). Dentro do Elemento HTML do Wix, porém, ele fica preso ao fim do elemento, junto ao rodapé, e não acompanha a rolagem. Para o botão seguir a tela no celular, crie também no próprio Wix um botão com o ícone do WhatsApp, marque *Fixar na tela* (canto inferior direito) e aponte para o mesmo link da página. Nesse caso, mude `botaoFlutuante` para `false` para não ficarem dois botões no fim da página:
   `https://wa.me/554130726994?text=Ol%C3%A1%20Tenho%20interesse%20em%20saber%20mais%20sobre%20Invisalign.%20*N%C3%83O%20APAGUE%20ESSA%20MENSAGEM%20VOC%C3%8A%20TEM%20PREFER%C3%8ANCIA*`

---

## 3. Rastreamento de conversões (Google Ads) · pendente dos IDs

A página roda dentro de um iframe do Wix, em outro domínio. Uma tag do Google Ads colocada dentro dela **não** é atribuída ao anúncio. Por isso o esquema funciona assim:

1. Cada clique em um botão do WhatsApp da landing page envia um aviso (`postMessage`) para o site Wix, informando **qual** botão foi clicado: `topo`, `hero`, `beneficios`, `indicacoes`, `como-funciona`, `dra`, `faq`, `contato` ou `final`.
2. O código de `wix-codigo-personalizado.html` recebe esse aviso. Ele vai em *Configurações > Código personalizado > Head*, só na página da landing page, e só funciona no site **publicado**, não no Visualizar. Escolha **um** caminho na variável `MODO`, nunca os dois, para não contar a conversão em dobro:
   - `'gtm'` (recomendado): envia o evento `lp_whatsapp_click` ao Google Tag Manager, e a tag de conversão fica no GTM;
   - `'gtag'`: o próprio código carrega a tag do Google Ads e registra a conversão. Nesse caso, preencha `GOOGLE_ADS_SEND_TO`.

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
- A página identifica a profissional (nome e CRO-PR 26722), a clínica (CRO-PR 6780 e CNPJ) e o responsável técnico. **O RT precisa ser confirmado antes de publicar.**
- Não há promessa de resultado. O texto deixa claro que a indicação depende de avaliação.
- Não há críticas ao aparelho fixo (art. 44 proíbe desmerecer técnicas de colegas). O texto apenas descreve os benefícios dos alinhadores.
- Ortopedia Funcional aparece como **área de atuação**, não como formação ou especialidade, porque isso não foi confirmado. Se a Dra. tiver título registrado no CRO, dá para ajustar.
- "Invisalign Doctor" aparece como está, sem acrescentar "certificada" ou níveis que não foram informados.
- "Invisalign" e "ClinCheck" aparecem com ® e com a nota de marca registrada da Align Technology. **Não use o logotipo oficial do Invisalign** sem o kit de marca fornecido pela Align ao Invisalign Doctor.
- Antes e depois somente com autorização assinada, sem edição de imagem (Res. CFO-196/2019).

## 5. Pendências

- [x] Fotos da Dra. (prontas em `imagens/`; falta subir no Wix e colar as URLs)
- [ ] Logo em PNG sem fundo, da **Clínica Ateliê Dental** (a logo recebida é da Ateliê Facial)
- [ ] Fotos da clínica (opcional)
- [ ] Casos de antes e depois, com TCLE assinado (sem nome do paciente), e consulta ao CRO-PR sobre publicação no site da clínica
- [ ] Depoimentos reais do Google e nota
- [x] Detalhes da consulta de avaliação (virou a seção "A consulta de avaliação")
- [x] Responsável técnico confirmado no CRO-PR
- [ ] URL da política de privacidade
- [ ] IDs do Google Ads e do GTM
- [ ] Cores oficiais da marca: a paleta está em variáveis no início do `<style>` (`--brand`, `--accent` etc.) e pode ser trocada em um minuto
