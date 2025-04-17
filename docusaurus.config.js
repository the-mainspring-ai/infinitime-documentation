// @ts-check
import { themes as prismThemes } from "prism-react-renderer";

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Introduction",
  tagline: "Documentation for the InfiniTime Online Project",
  favicon: "favicon.ico",

  // Your custom domain; ensure a static/CNAME file contains 'infinitimeonline.net'
  url: "https://infinitimeonline.net",
  baseUrl: "/",

  organizationName: "the-mainspring-ai", // GitHub org
  projectName: "infinitime-documentation", // Repo name
  deploymentBranch: "gh-pages", // GitHub Pages branch
  trailingSlash: false, // No trailing slash in URLs

  onBrokenLinks: "warn",
  onBrokenMarkdownLinks: "warn",

  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          // Fixed "Edit this page" link for the new repo location
          editUrl:
            "https://github.com/the-mainspring-ai/infinitime-documentation/tree/main/",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: "img/docusaurus-social-card.jpg",
      navbar: {
        title: "InfiniTime Documentation",
        logo: {
          alt: "InfiniTime Logo",
          src: "infinitime-logo.png",
        },
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
            items: [
              {
                label: "Documentation",
                to: "/docs/intro",
              },
            ],
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
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
