// @ts-check
import { themes as prismThemes } from "prism-react-renderer";

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Introduction",
  tagline: "Documentation for the InfiniTime Online Project",
  favicon: "favicon.ico",

  // ── Use project site URL (not a custom domain) when publishing under
  //    https://the-mainspring-ai.github.io/infinitime-documentation/
  url: "https://the-mainspring-ai.github.io", // host for project sites :contentReference[oaicite:7]{index=7}
  baseUrl: "/infinitime-documentation/", // path with leading/trailing slash :contentReference[oaicite:8]{index=8}

  organizationName: "the-mainspring-ai", // GitHub org/user
  projectName: "infinitime-documentation", // Repo name
  deploymentBranch: "gh-pages", // Branch to which Docusaurus deploys
  trailingSlash: false, // avoid GitHub Pages adding extra slashes

  onBrokenLinks: "warn",
  onBrokenMarkdownLinks: "warn",

  i18n: { defaultLocale: "en", locales: ["en"] },

  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          editUrl:
            "https://github.com/the-mainspring-ai/infinitime-documentation/tree/main/",
        },
        theme: { customCss: require.resolve("./src/css/custom.css") },
      },
    ],
  ],

  themeConfig: {
    image: "img/docusaurus-social-card.jpg",
    navbar: {
      title: "InfiniTime Documentation",
      logo: { alt: "InfiniTime Logo", src: "infinitime-logo.png" },
      items: [
        {
          to: "https://version9.infinitimeonline.net/InfiniTime/winLoginWindow.aspx",
          label: "Infinitime App",
          position: "right",
        },
        {
          href: "https://github.com/the-mainspring-ai/infinitime-documentation",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Docs",
          items: [{ label: "Documentation", to: "/docs/intro" }],
        },
        {
          title: "More",
          items: [
            {
              label: "GitHub",
              href: "https://github.com/the-mainspring-ai/infinitime-documentation",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} InfiniTime Project.`,
    },
    prism: { theme: prismThemes.github, darkTheme: prismThemes.dracula },
  },
};

export default config;
