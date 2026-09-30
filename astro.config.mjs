import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

function rehypeLazyImages() {
  const walk = (node) => {
    if (!node || typeof node !== "object") return;
    if (node.type === "element" && node.tagName === "img") {
      node.properties = node.properties || {};
      if (!node.properties.loading) node.properties.loading = "lazy";
      if (!node.properties.decoding) node.properties.decoding = "async";
    }
    for (const child of node.children || []) walk(child);
  };
  return (tree) => walk(tree);
}

export default defineConfig({
  site: "https://www.meghanfabulous.com",
  trailingSlash: "never",
  integrations: [sitemap()],
  markdown: {
    rehypePlugins: [rehypeLazyImages],
  },
});
