# 📚 Meu repositório de estudos - TDD

Repositório para praticar exercícios do curso ["Hands-On Test Driven Development with Python"](https://www.udemy.com/course/hands-on-test-driven-development-with-python/)  na plataforma [Udemy](https://www.udemy.com/).


## 🚦Test-driven development (benefício a longo prazo)



### - O que é? 🤔

Basicamente se baseia em pequenos ciclos de desenvolvimento, onde para cada nova funcionalidade desenvolvida escreve-se primeiros os testes antes mesmo de qualquer código. O teste inicial irá falhar(Red), então escrevemos um código que fará o teste passar(Green). Após o teste passar, é feita a refatoração(Refactor), onde as boas práticas serão aplicadas garantindo um código limpo, coeso e com baixo acoplamento. 


### - Por que? 🤔

Utilizar TDD duranto o desenvolvimento do seu projeto pode ter muitos benefícios como: 

- Feedback instantâneo sobre funcionalidades.
- Código mais limpo.
- Mais confiança durante a refatoração do código.
- Mais confiança durante a correção de bugs.
- Maior produtividade, já que gastará menos tempo caçando bugs e com depuradores.
- Ajuda a documentar aquilo que está sendo feito, melhorando o entendimento do propósito do código.


### ✔️ Boas Práticas

- Escreva testes claros e confiáveis, livres de bugs e que acompanhem o desenvolvimento do projeto. Lembre-se, nós passamos mais tempo lendo códigos que escrevendo.
- Mantenha os testes simples (Baby Steps).
- Escreva nomes descritivos para os testes, que descrevam de maneira simples e clara aquilo que esta sendo testado.
- Você deve ter uma meta de 100% de cobertura de código em funções com lógica real, evitando testar simples getters/setters.
- Execute seus testes com frequência para garantir que você nao tenha testes que falham intermitentemente.
- Evite dependências entre os testes. Executa-los de forma aleatória garantirá que seus testes não possuem dependências.
