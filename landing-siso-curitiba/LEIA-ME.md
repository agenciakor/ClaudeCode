# Landing page · Extração de siso em Curitiba (Dr. Delson Borsato)

Primeira página da série "uma landing por procedimento", para campanhas específicas no Google Ads.
Mesmo sistema visual da landing do Invisalign e da Home: paleta da marca, fontes Fahkwang e Montserrat,
botões, cards e carrossel iguais. Sem menu e sem rodapé do Wix (página de campanha).

| Arquivo | Para que serve |
|---|---|
| `index.html` | A landing completa. É **este arquivo inteiro** que vai no Elemento HTML da página. |
| `../landing-invisalign-vannessa/wix-codigo-personalizado.html` | Código personalizado do site (botão flutuante + rastreamento). Foi atualizado para reconhecer esta página; precisa ser colado de novo. |
| `preview/` | Prévia com imagens embutidas e prints, para aprovação. |

Tudo o que é editável fica no bloco `LP_CONFIG`, no começo do `index.html` (fotos, links, depoimentos, nota).

## Seções (de cima para baixo)

1. **Topo**: logo, "Dr. Delson Borsato · CRO-PR 23995" e botão do WhatsApp.
2. **Hero**: "Extração de siso com cirurgião bucomaxilofacial", foto do Dr. Delson, selos de residência e CRO.
3. **Faixa de credenciais**: residência, mestrado, nota 5,0 no Google e endereço.
4. **Quando o siso precisa sair**: 6 indicações (pericoronarite, incluso, mal posicionado, cárie recorrente, indicação ortodôntica, cistos).
5. **Quem faz a cirurgia**: formação hospitalar, sisos inclusos e próximos ao nervo, cirurgia no consultório, pós-operatório acompanhado.
6. **Como funciona**: avaliação, planejamento, cirurgia, pós-operatório, retorno.
7. **Recuperação**: 6 cards com o que esperar depois da cirurgia e aviso de que são orientações gerais.
8. **Dr. Delson**: currículo e CRO, com botão.
9. **Depoimentos**: carrossel com as mesmas avaliações do Google da Home (a da Amanda V., que cita os dois doutores e o pós-procedimento, vai primeiro).
10. **Clínica**: galeria, endereço, horário, WhatsApp, Instagram e mapa.
11. **Dúvidas frequentes**: 11 perguntas (dor, duração, 4 sisos de uma vez, siso incluso, exames, recuperação, trabalho, acompanhante, preço, avaliação).
12. **Chamada final** e **rodapé** com CRO da clínica, CNPJ, responsável técnica, cirurgião responsável e política de privacidade.

## Conformidade (CFO)

- Dr. Delson aparece como **cirurgião-dentista com residência em Cirurgia e Traumatologia Bucomaxilofacial**, nunca como "especialista" (só com a especialidade registrada no CRO-PR, Res. CFO-118/2012, art. 44).
- Sem preço, sem "sem dor" como promessa, sem garantia de resultado ou de tempo de recuperação; a página repete que a indicação depende da avaliação clínica e radiográfica.
- Rodapé com CRO da clínica, CNPJ, responsável técnica e cirurgião responsável.
- Sem fotos de antes e depois (se forem usadas um dia, só com TCLE e sem identificar o paciente, Res. CFO-196/2019).

## Como publicar no Wix

1. **Criar a página:** *Páginas e menu > + Adicionar página > Página em branco*. Nome: `Extração de Siso`.
2. **URL:** nas configurações da página (*... > Configurações > Informações da página* ou *SEO básico*), deixe o endereço final como `/extracao-de-siso-curitiba`. O código personalizado usa exatamente esse caminho para escolher a mensagem do WhatsApp.
3. **Ocultar do menu:** *... > Ocultar do menu*. A página é só para a campanha.
4. **Sem cabeçalho e rodapé:** *... > Configurações > Layout* (ou "Cabeçalho e rodapé") e desligue os dois, como na landing do Invisalign.
5. **SEO da página** (*Configurações > SEO básico*):
   - Título: `Extração de Siso em Curitiba | Dr. Delson Borsato – Clínica Ateliê Dental`
   - Descrição: `Extração de siso em Curitiba com cirurgião-dentista com residência em cirurgia bucomaxilofacial. Avaliação com exame de imagem, sisos inclusos e casos complexos, pós-operatório acompanhado. Agende pelo WhatsApp.`
   - "Mostrar esta página nos resultados de busca": **ligado** (ou desligado, se a página for usada só nos anúncios).
   - Opcional: um texto nativo do Wix marcado como H1 acima do bloco HTML: `Extração de siso em Curitiba · Clínica Ateliê Dental`, em Fahkwang 14 px, cor `#8A6136`.
6. **Elemento HTML:** *Adicionar > Incorporar código > HTML incorporado > Código*, cole o `index.html` inteiro, estique para a largura total e ajuste a altura (tabela abaixo). Para medir com precisão, troque `mostrarAltura: false` por `true`, leia o número vermelho no canto e volte para `false`.
7. **Versão mobile:** no editor de celular, selecione o bloco HTML e ajuste a altura também (a altura do desktop não vale para o celular).
8. **Código personalizado:** em *Configurações > Desenvolvimento e integrações > Código personalizado*, edite o trecho do botão e cole a versão nova do `wix-codigo-personalizado.html`. Ele reconhece esta página e usa a mensagem "Olá, quero agendar uma avaliação para extração de siso." no botão flutuante.
9. **Publicar** e testar no celular: botão flutuante, mensagem do WhatsApp, fotos e altura.

Alturas de referência (sem cabeçalho do Wix):

| Largura do elemento | Altura |
|---|---|
| 280 px (mobile clássico) | ≈ 18.900 px |
| 320 px (mobile clássico) | ≈ 17.600 px |
| 390 px | ≈ 16.400 px |
| 768 px | ≈ 12.900 px |
| 1024 px | ≈ 11.300 px |
| 1280 px | ≈ 11.100 px |
| 1440 px ou mais | ≈ 11.200 px |

## Rastreamento

Cada clique em WhatsApp envia ao site o evento `whatsapp_click` com `pagina: 'siso'` e `cta_posicao: 'siso_<posição>'`
(hero, indicacoes, como-funciona, dr, contato, faq, final, topo). O código personalizado converte em `lp_whatsapp_click` no GTM.
O botão flutuante envia `cta_posicao: 'siso_flutuante'`. Assim a campanha de siso fica separada da do Invisalign nos relatórios.

## Pendências e pontos a confirmar com a clínica

- [ ] **Sedação:** a página diz "anestesia local". Se a clínica oferecer sedação (consciente ou com anestesista), avisar para incluir.
- [ ] **Exames:** a página diz que o Dr. Delson "solicita os exames necessários". Se a clínica fizer radiografia panorâmica no local, avisar para destacar.
- [ ] **Quatro sisos na mesma sessão:** a página diz que "em alguns casos é possível". Confirmar a conduta do Dr. Delson.
- [ ] **Contato no pós-operatório:** a página diz que a equipe tira dúvidas pelo WhatsApp nos primeiros dias. Confirmar.
- [ ] **Convênios:** não há menção. Se a clínica atender planos odontológicos ou emitir recibo para reembolso, avisar para incluir no FAQ.
- [ ] **Fotos:** só há o retrato do Dr. Delson. Fotos dele em consulta ou em ambiente cirúrgico deixariam o hero e a seção "Quem faz a cirurgia" mais fortes.
- [ ] **Avaliações sobre sisos:** se houver avaliações no Google que citem extração de siso ou o Dr. Delson, mandar o texto para trocar no carrossel.
- [ ] **Especialidade registrada no CRO-PR:** continua pendente (vale para esta página e para a Home).
