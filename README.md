# Gitpod/codespace demo

This repo is contains demo and template scripts for using online tools
to create sharable and "ephemeral" coding environments.

Those are intended for quickly preparing the env without installation
from the client side. Gitpod is supposed to be also be useful for
collaborative development. Personally I think they are mostly geared
towards short-term teaching/demos.

| Tool      | Mini example                      | Link                                                   |
|-----------|-----------------------------------|--------------------------------------------------------|
| Gitpod    | `.gitpod.yml`                     | [![Open in Gitpod][gitpod_badge]][gitpod_url]          |
| Codespace | `.devcontainer/devcontainer.json` | [![Open in Codespace][codespace_badge]][codespace_url] |

[gitpod_badge]: https://img.shields.io/badge/open_in-gitpod-orange?style=flat-square&logo=gitpod
[gitpod_url]: https://gitpod.io/#https://github.com/yqshao/gitpod-demo
[codespace_badge]: https://img.shields.io/badge/open_in-codespace-black?style=flat-square&logo=github
[codespace_url]: https://codespaces.new/yqshao/gitpod-demo

## Try it out

This repo contains a small web application, try bringing up a terminal
with ```Ctrl+` ``` run `python mini-forum/app.py`, you can share the
app with others!

## Some detials

### Containers

+ Containers are defined by your configuration files; when you start a
  workspace it is prepared with the conatainer (and run some some extra
  steps).
+ You changes in each workspace will be saved even if you close the
  workspace. You are also reminded of your changes

### Cost

When you use Github code space, you wil consume the quota for both the
hour and storage you used, check:
https://github.com/settings/billing/summary

## Some information

+ Gitpod is an earlier provider of such develop-environment-as-code
  service, it is now moving away from the "classic model";
+ It looks like the free service from Gitpod is going away, and it
  will switch to service based on self-hosted runners;
+ Github Codespace later species the `devcontainer` format, which
  seems to gain more [adaptation][devcontainer_tools], including the
  new gitpod.

[devcontainer_tools]: https://containers.dev/supporting

## Other things might of interest

If all you want fits in jupyter notebooks, also consider [binder],
[google colab] (free gpus there), or alike...

[binder]: https://mybinder.org/
[google colab]: https://colab.research.google.com
