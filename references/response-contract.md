# Reply architecture contract

The response is the only source. Stable IDs let a diagram be regenerated without silently changing the reading map.

```yaml
response:
  id: r-response
  title: string
  language: zh-CN | en | other
  content_hash: string
  activation:
    triggered: boolean
    reasons: [length | section_density | multi_stage | user_requested]
    user_opt_out: boolean
  fragments:
    - id: r-p1
      kind: heading | paragraph | list | code | quote | table
      locator: paragraph index, heading path, or line range
      excerpt: string
  architecture:
    nodes: []
    edges: []
    diagram:
      direction: TD | LR
      mermaid: string
      fallback_outline: string
  reading_map: []
  render:
    placement: after_intro | before_detail | end
    renderer: mermaid | outline
    warnings: []
```

```yaml
node:
  id: a-goal
  label: string
  kind: goal | context | section | step | decision | output | risk | follow_up | other
  summary: string
  fragment_refs: [r-p1]
  confidence: 0..1
  provenance: extracted | ai_suggestion | user_edited
  status: confirmed | suggested

edge:
  id: r-e1
  from: a-context
  to: a-goal
  relation: leads_to | depends_on | decides | produces | constrains | explains | qualifies | other
  label: string
  fragment_refs: [r-p1, r-p2]
  confidence: 0..1
  provenance: extracted | ai_suggestion | user_edited
  status: confirmed | suggested
```

The first rendering can use `ai_suggestion` for inferred links. A user edit changes only the affected node or edge to `user_edited`; preserve the original suggestion in history if a persistent host supports it. A diagram node without a `fragment_ref` is invalid. The graph is a reading aid, so it may be incomplete, but it must not introduce unsupported content.
