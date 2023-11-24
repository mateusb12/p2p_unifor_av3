#### 1. Implementação do Algoritmo DFS
   - [X] **Preparação**: Antes de iniciar a visualização, implemente o algoritmo DFS de tal forma que você possa rastrear a ordem de visita dos nós.
   - [X] **Rastreamento**: Crie uma lista ou outra estrutura de dados que mantenha o registro de cada passo do algoritmo DFS para posterior animação.

#### 2. Preparação da Visualização do Grafo
   - [ ] **Posições dos Nós**: Calcule e armazene as posições dos nós usando o layout de sua escolha (por exemplo, `nx.spring_layout`).
   - [ ] **Dados dos Nós e Arestas**: Crie listas contendo as coordenadas dos nós e das arestas que serão usadas para desenhar o grafo em Plotly.

#### 3. Criação dos Quadros de Animação (Frames)
   - [ ] **Frames Individuais**: Para cada nó visitado pelo algoritmo DFS, crie um frame que destaque o nó atual e atenue os nós já visitados.
   - [ ] **Estilização**: Use diferentes estilos para mostrar o estado dos nós (por exemplo, visitado, atual, não visitado).

#### 4. Atualização da Figura com Frames de Animação
   - [ ] **Inclusão dos Frames**: Adicione todos os frames criados à figura do Plotly.
   - [ ] **Parâmetros da Animação**: Defina a duração de cada frame e as transições para criar o efeito de animação desejado.

#### 5. Controles de Reprodução da Animação
   - [ ] **Controles de Playback**: Adicione botões de controle para a animação, como reproduzir e pausar, para permitir que os usuários interajam com a animação.
   - [ ] **Configurações Interativas**: Configure as interações do usuário, como zoom e movimentação pelo grafo.

#### 6. Visualização e Interatividade
   - [ ] **Exibição do Grafo**: Use `pyo.iplot(fig)` para mostrar o grafo animado na interface do usuário.
   - [ ] **Testes**: Verifique se a animação funciona conforme esperado e ajuste os parâmetros conforme necessário para melhorar a visualização.

#### 7. Otimização e Refinamento
   - [ ] **Ajustes Finais**: Após testar a visualização, faça quaisquer ajustes finais para otimizar a apresentação e a clareza da animação DFS.
   - [ ] **Documentação**: Documente o código e as funções utilizadas para que outros possam entender e talvez expandir o trabalho no futuro.