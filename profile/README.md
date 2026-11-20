<p align="center">
  <img src="https://raw.githubusercontent.com/Vision-Decision/Glance-X-Lite/main/assets/demo.gif" width="860" alt="Demo: 256 images, one request, a scan picks the right image, the view zooms in, and new requests find each target in it">
  <br>
  <sub>One request over 256 cached images (68 ms on one GPU) picks the image; then new requests find their targets
  inside it. Every box, score, ranking and timing is a real Glance-X-Lite output on held-out images.
  <a href="https://github.com/Vision-Decision/Glance-X-Lite/blob/main/assets/demo.mp4">MP4 version</a> · made with <a href="https://github.com/Vision-Decision/Glance-X-Lite/blob/main/demo/render_story.py"><code>demo/</code></a> ·
  images from MS COCO.</sub>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img src="assets/hero-light.svg" width="100%" alt="Vision-Decision builds Glance, which answers many questions about one image in one forward pass, returning typed decisions: a box, yes or no, a choice, or not there. A typical VLM decodes free text token by token for every question; Glance stops after prefill and reads every answer from heads.">
</picture>

<p align="center">
  视觉决策模型：一次前向，回答一张图上的许多问题。
</p>

### Why

Agents mostly need decisions, not prose: *Where is the button? Is it there at all? Which clip shows it?* Generative VLMs write every answer token by token, which is slow and turns "not there" into a guess; Glance reads them all from one pass.

### Highlights

- **ScreenSpot-Pro accuracy 50.1 → 68.75 with the same Glance weights, no extra training.** Two inference-time controls do it: per-request adapter strength and in-block zoom.
- **Calibrated "not there".** Presence is read by a trained head and calibrated to a stated error rate, instead of left to the decoder.
- **Faster than bf16 vLLM and SGLang in 65 / 65 workloads.** glance-engine wins on every image, GUI, video and multi-client workload we measured.

### Getting started

1. Read the [Glance-4B-preview model card](https://huggingface.co/Vision-Decision/Glance-4B-preview) on Hugging Face.
2. Check the [Glance repo](https://github.com/Vision-Decision/Glance) for setup and examples.

### Projects

**Models**

- [**Glance**](https://github.com/Vision-Decision/Glance): a 4B decision VLM built on Qwen3.5-4B. One pass answers many typed questions about an image.
- [**Glance-X**](https://github.com/Vision-Decision/Glance-X): two-way grounding, text → box and box → text, in [4B](https://huggingface.co/Vision-Decision/Glance-X-4B) and [Lite](https://huggingface.co/Vision-Decision/Glance-X-Lite) sizes.

**Data**

- [**Glance-Data**](https://github.com/Vision-Decision/Glance-Data): grounding data with exact boxes, many phrasings, Chinese requests, hard negatives and multi-target queries, also on [Hugging Face](https://huggingface.co/datasets/Vision-Decision/Glance-Data).

**Systems** (opening soon)

- **glance-engine**: serving engine for decision models. Many questions per image, or one question over many cached images or clips.
- **glance-core**: model package, training, data builders and evaluation for Glance.
- **glance-video**: Glance for video, a clip-scanning search tool that agents can call.

<sub>Questions or ideas? Open an issue on [Glance](https://github.com/Vision-Decision/Glance/issues). Licenses: see each repository.</sub>
