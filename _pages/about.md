---
layout: about
title: about
permalink: /
subtitle: PhD Research Scholar · Computer Engineering

selected_papers: true
social: false

announcements:
  enabled: false
  scrollable: true
  limit: 3

latest_posts:
  enabled: false
---

<style>
  .scholar-profile {
    display: grid;
    grid-template-columns: 172px minmax(0, 1fr);
    align-items: center;
    gap: 1.5rem;
    max-width: 920px;
    margin: 0 auto 2rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--global-divider-color);
  }

  .scholar-profile__portrait {
    width: 172px;
    aspect-ratio: 4 / 5;
    overflow: hidden;
    border: 1px solid var(--global-divider-color);
    border-radius: 4px;
    background: var(--global-card-bg-color, #fff);
  }

  .scholar-profile__portrait img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center 28%;
  }

  .scholar-profile__copy {
    min-width: 0;
  }

  .scholar-profile__copy p {
    margin: 0 0 0.9rem;
    line-height: 1.65;
    text-align: left;
  }

  .scholar-profile__links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem 0.75rem;
    font-size: 0.9rem;
  }

  @media (max-width: 640px) {
    .scholar-profile {
      grid-template-columns: 1fr;
      gap: 1rem;
      margin-bottom: 1.5rem;
    }

    .scholar-profile__portrait {
      width: 142px;
      margin: 0 auto;
    }
  }
</style>

<div class="scholar-profile">
  <div class="scholar-profile__portrait">
    <img src="{{ '/assets/img/prof_pic.jpeg' | relative_url }}" alt="Portrait of Sambou KONE" loading="eager">
  </div>
  <div class="scholar-profile__copy">
    <p>I am <strong>Sambou KONE</strong>, a PhD Research Scholar in Computer Engineering at Alliance School of Computing, Bangalore. My research focuses on cyber-physical systems, embodied AI, and autonomous decision-making, with an emphasis on building intelligent systems that can perceive, reason, and act reliably in real-world environments under uncertainty. I am particularly interested in the integration of learning, perception, and control for robust deployment in dynamic and physically grounded settings.</p>
    <p class="scholar-profile__links"><a href="mailto:ksambouphd726@stu.alliance.edu.in">Email</a><a href="{{ '/phd/' | relative_url }}">Research profile</a><a href="{{ '/cv/' | relative_url }}">CV</a><a href="{{ '/publications/' | relative_url }}">Publications</a></p>
  </div>
</div>

## Research focus

<style>
  #research-focus + style + ul strong {
    color: var(--global-theme-color);
    background-color: rgba(31, 58, 95, 0.08);
    background-color: color-mix(in srgb, var(--global-theme-color) 10%, transparent);
    border-radius: 3px;
    padding: 0.08em 0.28em;
    -webkit-box-decoration-break: clone;
    box-decoration-break: clone;
  }
</style>

- **Cyber-physical systems** — sensing, computation, and control for robust operation in physical environments.
- **Embodied AI** — policies for agents that act through interaction with the world, not static inference alone.
- **LLMs / VLA** — language-guided perception and action for embodied agents.
- **Multimodal intelligence** — vision, signals, and context for robust perception and reasoning.
- **Autonomous systems** — adaptive planning and execution under uncertainty and dynamic constraints.
- **Artificial Intelligence of Things (AIoT)** — connecting devices, sensing, and adaptive intelligence.
- **Edge AI and TinyML** — efficient on-device inference under compute and power constraints.
- **Federated and Distributed Learning** — collaborative training across decentralized data and devices.
- **Edge–Fog–Cloud computing** — distributing computation from endpoints through gateways to cloud.
- **IoT and intelligent sensor networks** — connected sensing for real-time monitoring and response.
- **Digital Twins and intelligent systems** — data-linked models for simulation, prediction, and control.
- **AI/IoT applications for environmental monitoring, energy, smart cities and industry** — connected intelligence for real-world challenges.

## Education

**PhD, Computer Engineering** — Alliance School of Computing, Bangalore, 2026 to present

**B.Tech, Electronics & Communication Engineering** — Jain University × Texas Instruments, Bangalore, 2020–2024

**B.Eng., Computer & Telecom Engineering** — ENI-ABT, Bamako, 2016–2019

See <a href="{{ '/cv/' | relative_url }}">CV</a> for the full academic and professional background.

---

I am interested in collaborations on embodied perception, multimodal learning, and the real-world deployment of autonomous intelligent systems.
