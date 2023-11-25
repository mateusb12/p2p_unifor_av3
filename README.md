
# Roadmap/Backlog do Projeto - Algoritmos de Busca em Sistemas P2P

## Implementação Geral
- [X] Implementar um algoritmo capaz de criar e gerenciar uma rede P2P não estruturada.
- [ ] Realizar testes comparativos entre os diferentes algoritmos de busca, indicando o mais eficiente.
- [ ] Preparar apresentação de slides com os resultados dos testes.

## Divisão de Tarefas

### Backlog Mateus
- [x] Leitura do arquivo de configuração para a rede P2P (formato JSON).
  - `num_nodes`, `min_neighbors`, `max_neighbors`, `resources`, `edges`.
- [x] Implementação do algoritmo de verificação de integridade da rede:
  - [x] Rede não particionada.
  - [x] Limites de vizinhos respeitados.
  - [x] Nós com recursos.
  - [x] Sem arestas redundantes.
- [ ] Implementação da funcionalidade de busca por inundação (`flooding`):
  - [X] Implementar mecanismo de propagação de solicitações.
  - [X] Definir e aplicar o parâmetro TTL (Time To Live).
  - [X] Manter uma lista de nós visitados para evitar visitas repetidas.
  - [X] Verificar se o recurso de fato foi encontrado em cada nó e interromper a busca se encontrado.
- [ ] Implementação da funcionalidade de busca informada por inundação (`informed_flooding`):
  - [ ] Utilizar cache local para acelerar a busca.
  - [ ] Implementar a lógica de decisão baseada nas informações prévias.
  - [ ] Otimizar o algoritmo para reduzir o tráfego na rede.
- [ ] Desenvolvimento dos testes para as funcionalidades implementadas.

### Backlog Ísis
- [ ] Implementação do algoritmo de busca por passeio aleatório (`random_walk`):
  - [ ] Implementar a escolha aleatória de nós vizinhos.
  - [ ] Aplicar limitação de busca baseada no TTL.
  - [ ] Registrar o caminho percorrido em uma lista.
- [ ] Implementação do algoritmo de busca informada por passeio aleatório (`informed_random_walk`):
  - [ ] Integrar informações de cache local na seleção dos nós.
  - [ ] Otimizar a busca baseada em conhecimento prévio.
  - [ ] Implementar lógica adaptativa baseada em resultados anteriores.
- [ ] Implementação da interface para a iniciação da busca na rede P2P:
  - [ ] Desenvolver interface de usuário para parâmetros de busca.
  - [ ] Integrar sistema de logs para monitoramento das buscas.
- [ ] Implementação das funcionalidades opcionais:
  - [X] Representação gráfica da rede P2P.
  - [ ] Animação da rede P2P mostrando nós e mensagens.
  - [ ] Ferramentas de diagnóstico e análise de performance.
- [ ] Desenvolvimento dos testes para as funcionalidades implementadas.

## Entrega Final
- [ ] Organizar os resultados dos testes em tabelas/gráficos para a apresentação.
- [ ] Finalizar a apresentação de slides.
- [ ] Demonstração ao vivo do programa para diferentes topologias e configurações da rede P2P.
