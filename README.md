### O que deverá ser entregue:

- Uma aplicação Web com as seguintes funções:
  - [x] Tela de login com validação de usuário;
  - [x] Tela de cadastro de usuários (somente para usuário Admin);
  - [x] Tela de edição e remoção de usuários (somente para usuário Admin);
  - [x] Tela para cadastro de sensores e atuadores (somente para usuário Admin);
  - [x] Tela para edição e remoção de sensores e atuadores (somente para usuário Admin);
  - [x] Tela para visualização dos dados em Tempo Real (todos usuários tem acesso) coletados via MQTT Flask oriundos de uma aplicação do     RA1, sendo por sistema físico (ESP32 por exemplo) ou via Wokwi;
  - [x] Tela para comandos remotos (todos usuários tem acesso) utilizando Flask mqtt para publicar na aplicação em ESP32 ou Wokwi;

### Requisitos mínimos da Fase 2 do PjBL:

- [x] Utilização de Flask;
- [x] Uso do framework, layouts e componentes estudados no TDE2;
- [x] CRUD para usuários, sensores e atuadores;
- [x] Comunicação com Broker MQTT para realizar funções subscribe e publish;
- [x] Realizar comandos remotos pela aplicação desenvolvida em Flask;
- [x] Ausência de bugs;
- Respeitar as seguintes regras:
  - [x] Somente um usuário Admin;
  - [x] Somente Admin pode criar, editar e deletar usuários, sensores e atuadores;
  - [x] Somente Admin pode listar usuários;
  - [x] Todos usuários podem listar sensores e atuadores e acessar dashboards de recebimento de dados via MQTT Flask;
  - [x] Todos usuários podem acessar tela de comandos remotos via MQTT Flask para enviar dados ao BROKER.
