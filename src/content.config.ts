import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const journal = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/journal" }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    author: z.string().default("Meghan Fabulous"),
    description: z.string(),
    originalPath: z.string().optional(),
  }),
});

const eras = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/eras" }),
  schema: z.object({
    title: z.string(),
    years: z.string(),
    order: z.number(),
    summary: z.string(),
    next: z.string().optional(),
    lead: z.string().optional(),
    leadAlt: z.string().optional(),
    lookbooks: z.array(z.string()).default([]),
    facts: z
      .array(
        z.object({
          label: z.string(),
          text: z.string(),
          source: z.string(),
          url: z.string().optional(),
        }),
      )
      .default([]),
  }),
});

export const collections = { journal, eras };
