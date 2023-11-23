# Roadmap/Backlog do Projeto - Algoritmos de Busca em Sistemas P2P

## Implementação Geral
- [ ] Implementar um programa para criar e gerenciar uma rede P2P não estruturada.
- [ ] Realizar testes comparativos entre diferentes algoritmos de busca.
- [ ] Preparar apresentação de slides com resultados dos testes.

## Divisão de Tarefas

### Backlog Mateus
- [ ] Leitura do arquivo de configuração para a rede P2P (formato JSON).
  - `num_nodes`, `min_neighbors`, `max_neighbors`, `resources`, `edges`.
- [ ] Implementação da verificação de integridade da rede:
  - Rede não particionada.
  - Limites de vizinhos respeitados.
  - Nós com recursos.
  - Sem arestas redundantes.
- [ ] Implementação da funcionalidade de busca por inundação (`flooding`) e busca informada por inundação (`informed_flooding`).
- [ ] Desenvolvimento dos testes para as funcionalidades implementadas.

### Backlog Ísis
- [ ] Implementação do algoritmo de busca por passeio aleatório (`random_walk`) e busca informada por passeio aleatório (`informed_random_walk`).
- [ ] Implementação da interface para iniciação da busca na rede P2P:
  - `node_id`, `resource_id`, `ttl`, `algo`.
- [ ] Implementação das funcionalidades opcionais:
  - Representação gráfica da rede P2P.
  - Animação da rede P2P mostrando nós e mensagens.
- [ ] Desenvolvimento dos testes para as funcionalidades implementadas.

## Entrega Final
- [ ] Compilação dos resultados dos testes em tabelas/gráficos para a apresentação.
- [ ] Finalização da apresentação de slides.
- [ ] Demonstração ao vivo do programa para diferentes topologias e configurações da rede P2P.
