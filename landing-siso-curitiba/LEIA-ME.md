# Landing page · Extração de siso em Curitiba

Primeira página da série "uma landing por procedimento", para campanhas específicas no Google Ads.
Mesmo sistema visual da landing do Invisalign e da Home: paleta da marca, fontes Fahkwang e Montserrat,
botões, cards e carrosséis iguais. A página do Wix fica **com o cabeçalho principal do site** (menu) e
o rodapé é o próprio da landing, com os dados obrigatórios do CFO.

| Arquivo | Para que serve |
|---|---|
| `index.html` | A landing completa (sem cabeçalho próprio). É **este arquivo inteiro** que vai no Elemento HTML da página. |
| `../landing-invisalign-vannessa/wix-codigo-personalizado.html` | Código personalizado do site (botão flutuante + rastreamento). Foi atualizado para reconhecer esta página; precisa ser colado de novo. |
| `preview/` | Prévia com imagens embutidas, para aprovação. |

Tudo o que é editável fica no bloco `LP_CONFIG`, no começo do `index.html` (fotos, links, depoimentos, nota).

## Decisões de conteúdo (13/10)

- **Só a cirurgia é atribuída ao Dr. Delson.** A avaliação pode ser feita por outros profissionais da clínica, então a página fala em "avaliação" e "equipe", e em "cirurgia feita pelo Dr. Delson".
- **Uma única seção sobre o profissional** ("Tirar o siso é uma cirurgia. Aqui, é feita por quem se dedica a ela."), com a foto do Dr. Delson, currículo e os quatro diferenciais.
- **Fotos da clínica em carrossel** (3 por vez no desktop, 2 no tablet, 1 no celular), igual ao carrossel de depoimentos.
- **Foto da seção de indicações:** cadeira odontológica com a vista da cidade. No celular essa foto fica oculta, para não interromper a lista; ela aparece no carrossel da clínica.

## Seções (de cima para baixo)

1. **Hero**: "Extração de siso em Curitiba, do caso simples ao siso incluso", foto do Dr. Delson, selos de residência e CRO.
2. **Faixa de credenciais**: residência, mestrado, nota 5,0 no Google e endereço.
3. **Quando o siso precisa sair**: 6 indicações (pericoronarite, incluso, mal posicionado, cárie recorrente, indicação ortodôntica, cistos).
4. **Quem faz a cirurgia**: Dr. Delson, currículo e diferenciais (formação hospitalar, sisos inclusos e próximos ao nervo, cirurgia no consultório, pós-operatório acompanhado).
5. **Como funciona**: avaliação, planejamento, cirurgia, pós-operatório, retorno.
6. **Recuperação**: 6 cards com o que esperar depois da cirurgia e aviso de que são orientações gerais.
7. **Depoimentos**: carrossel com as avaliações do Google da Home (a da Amanda V., que cita os dois doutores e o pós-procedimento, vai primeiro).
8. **Clínica**: carrossel de fotos, endereço, horário, WhatsApp, Instagram e mapa.
9. **Dúvidas frequentes**: 11 perguntas (dor, duração, 4 sisos de uma vez, siso incluso, exames, recuperação, trabalho, acompanhante, preço, avaliação).
10. **Chamada final** e **rodapé** com CRO da clínica, CNPJ, responsável técnica, cirurgião responsável e política de privacidade.

## Conformidade (CFO)

- Dr. Delson aparece como **cirurgião-dentista com residência em Cirurgia e Traumatologia Bucomaxilofacial**, nunca como "especialista" nem "cirurgião bucomaxilofacial" (só com a especialidade registrada no CRO-PR, Res. CFO-118/2012, art. 44).
- Sem preço, sem "sem dor" como promessa, sem garantia de resultado ou de tempo de recuperação; a página repete que a indicação depende da avaliação clínica e radiográfica.
- Cursos de aperfeiçoamento e imersão **não** entram nesta página (o CFO só prevê, em publicidade, especialidades registradas e títulos stricto sensu). Ficam residência e mestrado.
- Rodapé com CRO da clínica, CNPJ, responsável técnica e cirurgião responsável.
- Sem fotos de antes e depois (se forem usadas um dia, só com TCLE e sem identificar o paciente, Res. CFO-196/2019).

## Como publicar no Wix

1. **Criar a página:** *Páginas e menu > + Adicionar página > Página em branco*. Nome: `Extração de Siso`.
2. **URL:** nas configurações da página (*... > Configurações > SEO básico*), deixe o endereço final como `/extracao-de-siso-curitiba`. O código personalizado usa exatamente esse caminho para escolher a mensagem do WhatsApp.
3. **Ocultar do menu:** *... > Ocultar do menu*. A página é só para a campanha (pode entrar no menu depois, em Especialidades).
4. **Cabeçalho:** a página fica **com o cabeçalho do site** (padrão do Wix). O rodapé do Wix pode ficar ou não: a landing já tem rodapé próprio com os dados do CFO. Se os dois ficarem, o do Wix aparece abaixo do da landing.
5. **SEO da página** (*Configurações > SEO básico*):
   - Título: `Extração de Siso em Curitiba | Clínica Ateliê Dental · Dr. Delson Borsato`
   - Descrição: `Extração de siso em Curitiba, do caso simples ao siso incluso. Cirurgia feita por cirurgião-dentista com residência em cirurgia bucomaxilofacial, avaliação com exame de imagem e pós-operatório acompanhado. Agende pelo WhatsApp.`
   - "Mostrar esta página nos resultados de busca": **ligado** (ou desligado, se a página for usada só nos anúncios).
   - Recomendado: um texto nativo do Wix marcado como H1 acima do bloco HTML: `Extração de siso em Curitiba · Clínica Ateliê Dental`, em Fahkwang 14 px, cor `#8A6136`. O Google não lê o conteúdo do Elemento HTML como parte da página.
6. **Elemento HTML:** *Adicionar > Incorporar código > HTML incorporado > Código*, cole o `index.html` inteiro, estique para a largura total e ajuste a altura (tabela abaixo). Para medir com precisão, troque `mostrarAltura: false` por `true`, leia o número vermelho no canto e volte para `false`.
7. **Versão mobile:** no editor de celular, selecione o bloco HTML e ajuste a altura também (a altura do desktop não vale para o celular).
8. **Código personalizado:** em *Configurações > Desenvolvimento e integrações > Código personalizado*, edite o trecho do botão e cole a versão nova do `wix-codigo-personalizado.html`. Ele reconhece esta página e usa a mensagem "Olá, quero agendar uma avaliação para extração de siso." no botão flutuante.
9. **Publicar** e testar no celular: menu do site, botão flutuante, mensagem do WhatsApp, carrosséis, fotos e altura.

Alturas de referência (só o Elemento HTML, sem o cabeçalho do Wix):

| Largura do elemento | Altura |
|---|---|
| 280 px (mobile clássico) | ≈ 16.600 px |
| 320 px (mobile clássico) | ≈ 15.100 px |
| 390 px | ≈ 13.700 px |
| 768 px | ≈ 11.400 px |
| 1024 px | ≈ 10.500 px |
| 1280 px | ≈ 10.300 px |
| 1440 px ou mais | ≈ 10.400 px |

## Rastreamento

Cada clique em WhatsApp envia ao site o evento `whatsapp_click` com `pagina: 'siso'` e `cta_posicao: 'siso_<posição>'`
(hero, indicacoes, cirurgiao, como-funciona, contato, faq, final). O código personalizado converte em `lp_whatsapp_click`
no GTM, com os campos `cta_posicao` e `pagina`. O botão flutuante envia `cta_posicao: 'siso_flutuante'`.
Assim a campanha de siso fica separada da do Invisalign nos relatórios.

## Pendências e pontos a confirmar com a clínica

- [ ] **Sedação:** a página diz "anestesia local". Se a clínica oferecer sedação (consciente ou com anestesista), avisar para incluir.
- [ ] **Exames:** a página diz que "a equipe solicita os exames necessários". Se a clínica fizer radiografia panorâmica no local, avisar para destacar.
- [ ] **Quatro sisos na mesma sessão:** a página diz que "em alguns casos é possível". Confirmar a conduta do Dr. Delson.
- [ ] **Contato no pós-operatório:** a página diz que a equipe tira dúvidas pelo WhatsApp nos primeiros dias. Confirmar.
- [ ] **Convênios:** não há menção. Se a clínica atender planos odontológicos ou emitir recibo para reembolso, avisar para incluir no FAQ.
- [ ] **Nome do mestrado:** a página usa "Princípios da Cirurgia" (nome do programa na Faculdade Evangélica Mackenzie). A Home ainda diz "Princípios de Cirurgia"; alinhar na próxima atualização da Home.
- [ ] **Fotos:** só há o retrato do Dr. Delson (usado no hero e na seção do profissional). Fotos dele em consulta ou em ambiente cirúrgico deixariam a página mais forte.
- [ ] **Avaliações sobre sisos:** se houver avaliações no Google que citem extração de siso ou o Dr. Delson, mandar o texto para trocar no carrossel.
- [ ] **Especialidade registrada no CRO-PR:** continua pendente (vale para esta página e para a Home, onde o card do Dr. Delson diz "Sócio-proprietário · Cirurgia bucomaxilofacial").
