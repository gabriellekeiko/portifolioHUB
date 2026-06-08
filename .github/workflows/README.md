# PortfolioHUB | DevOps & CI/CD 

Este diretório é o centro de automação e infraestrutura do ecossistema PortfolioHUB. Aqui, transformamos scripts de deploy em uma esteira de entrega contínua automatizada, utilizando as melhores práticas de mercado para garantir estabilidade, segurança e eficiência a cada atualização.

## Roadmap de Automação

Navegue pelos módulos abaixo para explorar as competências de infraestrutura desenvolvidas neste workflow:

### Esteira de Integração e Entrega Contínuas (CI/CD)
* **Foco:** Automatizar o ciclo de vida de publicação do portfólio.
* **Tecnologias:** GitHub Actions, YAML, Ubuntu Virtual Runners.
* **Competências:** Configuração de gatilhos automáticos (`on: push`), gerenciamento de concorrência de servidores e deploy automático para o GitHub Pages a partir da branch `main`.
* **Destaque:** Eliminação completa de deploys manuais, garantindo sincronização em tempo real com segurança de ponta.

### Governança e Controle de Acesso (Least Privilege)
* **Foco:** Blindagem de segurança e controle estrito de permissões de tokens.
* **Tecnologias:** GitHub Security Tokens.
* **Competências:** Implementação de escopo restrito de segurança no container (`contents: read` para clonar o código e `pages: write` para publicar).
* **Destaque:** Alinhamento total com as políticas corporativas de menor privilégio.

---

## Tech Stack & Ferramentas

| Categoria | Tecnologias |
| :--- | :--- |
| **Linguagem Orquestradora** | YAML |
| **Ambiente de Build** | Ubuntu Latest (Linux Virtual Runner) |
| **Esteira Core** | GitHub Actions |
| **Segurança de Acesso** | GitHub OIDC & Scoped Tokens |

---

## Status da Automação

* 🟢 **Módulo CI/CD:** 100% Concluído (Deploy automatizado via `deploy.yml`)
* 🟢 **Módulo Governança:** 100% Concluído (Tokens de permissão restrita configurados)
* 🟢 **Módulo Multienviroment:** 100% Concluído (Testes automatizados integrados à branch `staging`)

---

## Conecte-se Comigo

Sinta-se à vontade para explorar os códigos da nossa esteira de automação e entrar em contato para colaborações ou insights técnicos.

* **LinkedIn:** [Gabrielle Keiko](https://www.linkedin.com/in/gabrielle-keiko-9baa6a2b3/))
* **Portfólio Web:** [Visualizar Interface Live](https://gabriellekeiko.github.io/portifolioHUB/)
* **E-mail Institucional:** gabrielle.keiko@sempreceub.com
* **E-mail Pessoal:** gkeiko.05@gmail.com
