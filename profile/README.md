<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
    <img src="assets/logo-light.svg" width="96" alt="Vision-Decision">
  </picture>
</p>

<h1 align="center">Vision-Decision</h1>

<p align="center">
  <b>Vision models that decide, not just describe.</b><br>
  Ask many questions about an image. Get typed answers (a box, yes / no, a choice, or <i>"it's not there"</i>) in one forward pass.
</p>

<p align="center">
  <a href="https://huggingface.co/Vision-Decision"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Vision--Decision-FFD21E" alt="Hugging Face"></a>
</p>

---

### Why

Agents that look at screens, photos and videos mostly need **decisions**: *Where is the button? Is the object there at all? Which of these clips shows it?*
Generative VLMs answer by writing text one token at a time. That is slow when you have many questions, and "not there" becomes a guess.
We build models and systems that read each decision straight from one shared pass over the image, so it is fast and the answer to "not there" can be calibrated.

### Projects

| | What it is | Links |
|---|---|---|
| **Glance** | A 4B decision VLM built on Qwen3.5-4B. One prefill answers many typed questions about an image. | [model](https://huggingface.co/Vision-Decision/Glance-4B-preview) · [repo](https://github.com/Vision-Decision/Glance) |
| **glance-engine** | Serving engine for decision models: many questions per image, one question over many cached images or clips. Faster than bf16 vLLM and SGLang in all 65 workloads we measured. | [repo](https://github.com/Vision-Decision/glance-engine) |
| **glance-core** | Model package, training, data builders and evaluation for Glance. | [repo](https://github.com/Vision-Decision/glance-core) |
| **glance-video** | Glance for video: a clip-scanning search tool that agents can call. | [repo](https://github.com/Vision-Decision/glance-video) |
| **Glance-Data** | Grounding data with exact boxes, many phrasings, Chinese requests, hard negatives and multi-target queries. | [repo](https://github.com/Vision-Decision/Glance-Data) · [dataset](https://huggingface.co/datasets/Vision-Decision/Glance-Data) |
| **Glance-X** | Two-way grounding model (text → box and box → text). | [repo](https://github.com/Vision-Decision/Glance-X) · [4B](https://huggingface.co/Vision-Decision/Glance-X-4B) · [Lite](https://huggingface.co/Vision-Decision/Glance-X-Lite) |

### Highlights

- **65 / 65:** glance-engine beats bf16 vLLM and SGLang on every image, GUI, video and multi-client workload we measured.
- **50.1 → 68.75 on ScreenSpot-Pro** with per-request adapter strength and in-block zoom, no extra training.
- **"Not there" as a first-class answer:** presence is read by a trained head and can be calibrated to a stated error rate, rather than left to the decoder.

<sub>Licenses are listed in each repository.</sub>
